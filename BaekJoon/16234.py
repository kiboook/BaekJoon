import sys
from copy import deepcopy
from collections import deque


def BFS(field, visit, start):
	dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
	visit[start[0]][start[1]] = 1
	move_idx = [start]
	queue = deque([start])
	population = field[start[0]][start[1]]

	while queue:
		now_i, now_j = queue.popleft()
		for val in dirs:
			visit_i, visit_j = now_i + val[0], now_j + val[1]
			if 0 <= visit_i < n and 0 <= visit_j < n and not visit[visit_i][visit_j]:
				if L <= abs(field[now_i][now_j] - field[visit_i][visit_j]) <= R:
					population += field[visit_i][visit_j]
					visit[visit_i][visit_j] = 1
					move_idx.append([visit_i, visit_j])
					queue.append([visit_i, visit_j])

	average = population // len(move_idx)
	for idx in move_idx:
		field[idx[0]][idx[1]] = average


def move(field):
	before_field = deepcopy(field)
	visit = [[0 for _ in range(n)] for _ in range(n)]

	for i in range(n):
		for j in range(n):
			if not visit[i][j]:
				BFS(field, visit, [i, j])

	if before_field == field:
		return False
	else:
		return True


def solution(field):
	move_cnt = 0
	while move(field):
		move_cnt += 1

	return move_cnt


if __name__ == '__main__':
	n, L, R = map(int, input().split())
	field = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(n)]

	print(solution(field))