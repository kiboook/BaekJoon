from collections import deque
from copy import deepcopy
import sys


def BFS(start, visit_world, world, after_world):
	queue = deque([start])
	visit_union = [[0] * N for _ in range(N)]
	visit_idx = [start]
	visit_world[start[0]][start[1]] = 1
	visit_union[start[0]][start[1]] = 1
	dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
	counrty_cnt = 1
	population = world[start[0]][start[1]]

	while queue:
		cur_i, cur_j = queue.popleft()
		for val in dirs:
			visit_i = cur_i + val[0]
			visit_j = cur_j + val[1]

			if 0 <= visit_i < N and 0 <= visit_j < N and visit_union[visit_i][visit_j] == 0:
				if L <= abs(world[cur_i][cur_j] - world[visit_i][visit_j]) <= R:
					counrty_cnt += 1
					population += world[visit_i][visit_j]
					queue.append([visit_i, visit_j])
					visit_idx.append([visit_i, visit_j])
					visit_world[visit_i][visit_j] = 1
					visit_union[visit_i][visit_j] = 1

	average_poppulation = population // counrty_cnt
	for idx in visit_idx:
		after_world[idx[0]][idx[1]] = average_poppulation

	return


def solution(world):
	answer = 0

	while True:
		after_world = deepcopy(world)
		visit = [[0] * N for _ in range(N)]

		for i in range(N):
			for j in range(N):
				if visit[i][j] == 0:
					BFS([i, j], visit, world, after_world)

		if world == after_world:
			return answer
		else:
			answer += 1
			world = after_world


if __name__ == '__main__':
	N, L, R = map(int, input().rsplit())
	world = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)]
	print(solution(world))