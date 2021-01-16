import sys
from collections import deque
from copy import deepcopy


def DFS(data, start, height):
	queue = deque([start])
	data[start[0]][start[1]] = 0
	dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

	while queue:
		cur_i, cur_j = queue.popleft()

		for val in dirs:
			visit_i = cur_i + val[0]
			visit_j = cur_j + val[1]
			if 0 <= visit_i < n and 0 <= visit_j < n and data[visit_i][visit_j] > height:
				data[visit_i][visit_j] = 0
				queue.append([visit_i, visit_j])
	return


def rain(height):
	copy_ground = deepcopy(ground)
	safe_area = 0

	for i in range(n):
		for j in range(n):
			if copy_ground[i][j] > height:
				DFS(copy_ground, [i, j], height)
				safe_area += 1

	return safe_area


if __name__ == '__main__':
	res = 0
	n = int(input())
	ground = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(n)]

	for i in range(0, 101):
		res = max(res, rain(i))

	print(res)