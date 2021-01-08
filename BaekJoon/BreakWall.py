import sys
from collections import deque


def findRoad():
	queue = deque([[0, 0, 0]])
	visit = [[[0, 0] for _ in range(m)] for _ in range(n)]
	visit[0][0][0] = 1

	while queue:
		cur_i, cur_j, wall = queue.popleft()
		if cur_i == n - 1 and cur_j == m - 1:
			return visit[cur_i][cur_j][wall]

		visit_dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
		for i in visit_dir:
			visit_i = cur_i + i[0]
			visit_j = cur_j + i[1]
			if 0 <= visit_i < n and 0 <= visit_j < m and visit[visit_i][visit_j][wall] == 0:
				if data[visit_i][visit_j] == 0:
					visit[visit_i][visit_j][wall] = visit[cur_i][cur_j][wall] + 1
					queue.append([visit_i, visit_j, wall])

					# 처음 벽을 만나는 경우
			if data[visit_i][visit_j] == 1 and wall == 0:
					visit[visit_i][visit_j][1] = visit[cur_i][cur_j][wall] + 1
					queue.append([visit_i, visit_j, 1])

	return -1


if __name__ == '__main__':
	n, m = map(int, input().split())
	data = []
	for _ in range(n):
		for val in sys.stdin.readline().rsplit():
			data.append([int(num) for num in val])

	print(findRoad())