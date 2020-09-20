import sys
from collections import deque


def escape_maze(arr, x, y):
	start = [x, y, 1]
	queue = deque([start])

	while queue:
		dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
		visit = queue.popleft()
		i, j, dist = visit[0], visit[1], visit[2]

		for cur in dirs:
			if 0 <= i + cur[0] < N and 0 <= j + cur[1] < M and arr[i + cur[0]][j + cur[1]] == 1:
				queue.append([i + cur[0], j + cur[1], dist + 1])
				arr[i + cur[0]][j + cur[1]] = dist + 1


N, M = map(int, input().rsplit())
_arr = [[int(x) for x in sys.stdin.readline().rsplit()[0]] for _ in range(N)]
escape_maze(_arr, 0, 0)

print(_arr[N - 1][M - 1])