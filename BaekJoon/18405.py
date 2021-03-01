import sys
from collections import deque


def inItVirus(n, k, field):
	init = []

	for i in range(n):
		for j in range(n):
			if field[i][j]:
				init[field[i][j]].append([field[i][j], 0, i, j])

	init.sort()
	return init


def solution(n, k, field, info):
	s, x, y = info
	dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
	viruses = inItVirus(n, k, field)
	queue = deque(viruses)

	while queue:
		virus, sec, now_i, now_j = queue.popleft()

		if sec == s:
			return field[x - 1][y - 1]

		for i in dirs:
			visit_i, visit_j = now_i + i[0], now_j + i[1]
			if 0 <= visit_i < n and 0 <= visit_j < n and field[visit_i][visit_j] == 0:
				field[visit_i][visit_j] = virus
				queue.append([virus, sec + 1, visit_i, visit_j])

	return field[x - 1][y - 1]


if __name__ == '__main__':
	n, k = map(int, input().split())
	field = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(n)]
	info = map(int, input().split())

	print(solution(n, k, field, info))