import sys
from collections import deque


def DFS(start, visit):
	queue = deque([start])
	visit[start[0]][start[1]] = 1
	dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

	while queue:
		cur_i, cur_j = queue.popleft()

		for val in dirs:
			visit_i = cur_i + val[0]
			visit_j = cur_j + val[1]

			if 0 <= visit_i < n and 0 <= visit_j < m:
				if data[visit_i][visit_j] > 0 and visit[visit_i][visit_j] == 0:
					visit[visit_i][visit_j] = 1
					queue.append([visit_i, visit_j])

	return


def count_iceberg():
	visit = [[0] * m for _ in range(n)]
	cnt = 0

	for i in range(n):
		for j in range(m):
			if data[i][j] > 0 and visit[i][j] == 0:
				DFS([i, j], visit)
				cnt += 1
	return cnt


def iceberg():
	ice = [[0] * m for _ in range(n)]
	dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

	for i in range(n):
		for j in range(m):
			if data[i][j] > 0:
				ice[i][j] = 1

				for val in dirs:
					visit_i = i + val[0]
					visit_j = j + val[1]

					if data[visit_i][visit_j] == 0 and ice[visit_i][visit_j] != 1:
						if data[i][j] != 0:
							data[i][j] -= 1

	return count_iceberg()


if __name__ == '__main__':
	n, m = map(int, input().split())
	data = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(n)]

	if count_iceberg() > 1:
		print(0)
		exit(0)

	year = 0
	while True:
		res = iceberg()
		year += 1

		if res >= 2:
			print(year)
			exit(0)

		if res == 0:
			print(0)
			exit(0)