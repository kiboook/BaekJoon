import sys
from copy import deepcopy
from itertools import combinations
import collections


def countSafeArea(area, virus):
	queue = collections.deque(virus)
	visit = [[-1, 0], [0, 1], [1, 0], [0, -1]]

	while queue:
		curLoc = queue.popleft()

		for val in visit:
			visitRow = curLoc[0] + val[0]
			visitCol = curLoc[1] + val[1]

			if 0 <= visitRow < n and 0 <= visitCol < m:
				if area[visitRow][visitCol] == 0:
					area[visitRow][visitCol] = 2
					queue.append([visitRow, visitCol])

	return collections.Counter(sum(area, []))[0]


n, m = map(int, input().split())
data = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(n)]
zeroIndex, virusIndex = [], []
safeArea = 0

for i in range(n):
	for j in range(m):
		if data[i][j] == 0:
			zeroIndex.append([i, j])
		if data[i][j] == 2:
			virusIndex.append([i, j])

wallIndex = combinations(zeroIndex, 3)

for val in wallIndex:
	copyData = deepcopy(data)
	wall1, wall2, wall3 = val

	copyData[wall1[0]][wall1[1]] = 1
	copyData[wall2[0]][wall2[1]] = 1
	copyData[wall3[0]][wall3[1]] = 1

	safeArea = max(safeArea, countSafeArea(copyData, virusIndex))

print(safeArea)