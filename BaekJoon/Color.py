import sys
from collections import deque
from copy import deepcopy


def change_color(arr, size):
	for i in range(size):
		for j in range(size):
			if arr[i][j] == 'R':
				arr[i][j] = 'G'


def start_BFS(arr, size):
	cnt = 0

	for i in range(size):
		for j in range(size):
			if arr[i][j] != 'V':
				BFS(arr, i, j)
				cnt += 1
	print(cnt)


def BFS(arr, i, j):
	queue = deque([[i, j]])
	start_color = arr[i][j]
	arr[i][j] = 'V'

	while queue:
		cur_i, cur_j = queue.popleft()
		dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

		for val in dirs:
			visit_i = cur_i + val[0]
			visit_j = cur_j + val[1]

			if 0 <= visit_i < size and 0 <= visit_j < size and arr[visit_i][visit_j] == start_color:
				queue.append([visit_i, visit_j])
				arr[visit_i][visit_j] = 'V'


size = int(input())
_arr = [[x for x in sys.stdin.readline().rsplit()[0]] for _ in range(size)]
start_BFS(deepcopy(_arr), size)
change_color(_arr, size)
start_BFS(_arr, size)

# 5
# RRRBR
# GGBBB
# BBBRR
# BBRRR
# RRRRR