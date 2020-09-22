import sys
from collections import deque


def check_tomato_min_day(arr, m, n):
	box = arr[:]
	row, col = n, m
	day = 0
	queue = deque()
	for i in range(row):
		for j in range(col):
			if box[i][j] == 1:
				queue.append([i, j, day])

	while queue:
		dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
		cur_i, cur_j, cur_day = queue.popleft()

		for val in dirs:
			visit_i = cur_i + val[0]
			visit_j = cur_j + val[1]

			if 0 <= visit_i < row and 0 <= visit_j < col and box[visit_i][visit_j] == 0:
				queue.append([visit_i, visit_j, cur_day + 1])
				box[visit_i][visit_j] = cur_day + 1

	for i in range(row):
		for j in range(col):
			if box[i][j] == 0:
				return -1

	return cur_day


in_m, in_n = map(int, input().rsplit())
in_arr = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(in_n)]
print(check_tomato_min_day(in_arr, in_m, in_n))