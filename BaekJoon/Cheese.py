import sys
from collections import deque


def findRoad(start):
	queue = deque([start])
	visit = [[0] * m for _ in range(n)]
	visit[start[0]][start[1]] = 1
	remove_cheese = 0

	dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
	while queue:
		cur_i, cur_j = queue.popleft()

		for val in dirs:
			visit_i = cur_i + val[0]
			visit_j = cur_j + val[1]
			if 0 <= visit_i < n and 0 <= visit_j < m:
				if data[visit_i][visit_j] == 0 and visit[visit_i][visit_j] == 0:
					visit[visit_i][visit_j] = 1
					queue.append([visit_i, visit_j])

				if data[visit_i][visit_j] > 0:
					data[visit_i][visit_j] += 1

	for i in range(n):
		for j in range(m):
			if data[i][j] >= 3:
				data[i][j] = 0
				remove_cheese += 1
			elif data[i][j] == 2:
				data[i][j] = 1

	if remove_cheese > 0:
		return True
	else:
		return False


if __name__ == '__main__':
	res = 0
	n, m = map(int, input().split())
	data = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(n)]

	while findRoad([0, 0]):
		res += 1

	print(res)
