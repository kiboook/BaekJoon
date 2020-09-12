import sys
from collections import deque


def BFS(arr, start_loc):
	home = 0
	queue = deque([start_loc])
	dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

	while queue:
		cur_i, cur_j = queue.popleft()
		arr[cur_i][cur_j] = 0
		home += 1

		for dir in dirs:
			go_i = cur_i + dir[0]
			go_j = cur_j + dir[1]

			if 0 <= go_i < len(arr) and 0 <= go_j < len(arr) and arr[go_i][go_j] == 1:
				queue.append([go_i, go_j])
				arr[go_i][go_j] = 0

	return home


def find_hometown(arr):
	hometown = []

	for i in range(len(arr)):
		for j in range(len(arr)):
			if arr[i][j] == 1:
				hometown.append(BFS(arr, [i, j]))

	print(len(hometown))
	for i in sorted(hometown):
		print(i)


N = int(input())
_arr = [[int(x) for x in sys.stdin.readline().rsplit()[0]] for _ in range(N)]
find_hometown(_arr)


# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000