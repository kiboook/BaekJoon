import sys
from collections import deque


def check_tomato(box, M, N, H):
	queue = deque()
	for h in range(H):
		for i in range(N):
			for j in range(M):
				if box[h][i][j] == 1:
					queue.append([h, i, j, 0])

	while queue:
		dirs = [[-1, 0, 0], [1, 0, 0], [0, 0, -1], [0, 0, 1], [0, 1, 0], [0, -1, 0]]
		cur_h, cur_i, cur_j, day = queue.popleft()

		for val in dirs:
			visit_h = cur_h + val[0]
			visit_i = cur_i + val[1]
			visit_j = cur_j + val[2]

			if 0 <= visit_h < H and 0 <= visit_i < N and 0 <= visit_j < M and box[visit_h][visit_i][visit_j] == 0:
				queue.append([visit_h, visit_i, visit_j, day + 1])
				box[visit_h][visit_i][visit_j] = day + 1

	for h in range(H):
		for i in range(N):
			for j in range(M):
				if box[h][i][j] == 0:
					return -1
	return day


M, N, H = map(int, input().rsplit())
_box = [[list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)] for _ in range(H)]
print(check_tomato(_box, M, N, H))