from collections import deque


def BFS(start):
	queue = deque([start])
	visit = [[0] * m for _ in range(n)]
	visit[start[0]][start[1]] = 1
	dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
	distance = 0

	while queue:
		cur_i, cur_j, weight = queue.popleft()
		distance = weight
		for val in dirs:
			visit_i = cur_i + val[0]
			visit_j = cur_j + val[1]
			if 0 <= visit_i < n and 0 <= visit_j < m and visit[visit_i][visit_j] == 0:
				if ground[visit_i][visit_j] == 'L':
					visit[visit_i][visit_j] = 1
					queue.append([visit_i, visit_j, weight + 1])

	return distance


def solution():
	output = 0

	for i in range(n):
		for j in range(m):
			if ground[i][j] == 'L':
				result = BFS([i, j, 0])
				if output < result:
					output = result

	return output


if __name__ == '__main__':
	n, m = map(int, input().rsplit())
	ground = [list(map(str, input())) for _ in range(n)]

	print(solution())

# 7 7
# WLLLLLW
# LWLWLWW
# LLLWLWW
# LWWWLWW
# LLLLLWW
# LWWWWWW
# WWWWWWW