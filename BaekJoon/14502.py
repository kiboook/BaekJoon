import sys
from itertools import combinations
from copy import deepcopy
from collections import deque
from collections import Counter


def BFS(viruses, field, walls, n, m):
	dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

	for wall in walls:
		field[wall[0]][wall[1]] = 1

	queue = deque([])
	for virus in viruses:
		queue.append(virus)
	while queue:
		now_i, now_j = queue.popleft()
		for i in dirs:
			visit_i, visit_j = now_i + i[0], now_j + i[1]
			if 0 <= visit_i < n and 0 <= visit_j < m:
				if field[visit_i][visit_j] == 0:
					field[visit_i][visit_j] = 2
					queue.append([visit_i, visit_j])

	return Counter(sum(field, []))[0]


def solution(n, m, field):
	answer = 0
	empty = []
	viruses = []
	for i in range(n):
		for j in range(m):
			if field[i][j] == 0:
				empty.append([i, j])
			if field[i][j] == 2:
				viruses.append([i, j])

	for wall in combinations(empty, 3):
		answer = max(answer, BFS(viruses, deepcopy(field), wall, n, m))

	return answer


if __name__ == '__main__':
	n, m = map(int, input().split())
	field = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(n)]
	print(solution(n, m, field))