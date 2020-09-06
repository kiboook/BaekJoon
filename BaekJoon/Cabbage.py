import sys
from collections import deque


def BFS(x, y):
	start_loc = [x, y]
	queue = deque([start_loc])
	dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]

	while queue:
		print(queue)
		i, j = queue.popleft()
		cabbage_map[i][j] = 0

		for dir in dirs:
			go_x, go_y = i + dir[0], j + dir[1]

			if 0 <= go_x < N and 0 <= go_y < M and cabbage_map[go_x][go_y] == 1:
				cabbage_map[go_x][go_y] = 0
				queue.append([go_x, go_y])

	return 1


T = int(input())

for _ in range(T):
	bugs = 0
	M, N, K = map(int, sys.stdin.readline().rsplit())
	cabbage_map = [[0] * M for _ in range(N)]

	for _ in range(K):
		x, y = map(int, sys.stdin.readline().rsplit())
		cabbage_map[y][x] = 1

	for x in range(N):
		for y in range(M):
			if cabbage_map[x][y] == 1:
				bugs += BFS(x, y)

	print(bugs)

# 1
# 10 10 9
# 3 1
# 4 1
# 5 1
# 3 2
# 4 2
# 5 2
# 3 3
# 4 3
# 5 3