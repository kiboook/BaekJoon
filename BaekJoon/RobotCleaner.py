import sys
from collections import deque


def clean():
	queue = deque([[robot_i, robot_j, head]])
	ground[robot_i][robot_j] = 3
	clean_cnt = 0
	north, east, south, west = [-1, 0], [0, 1], [1, 0], [0, -1]

	while queue:
		none_cnt = 0
		cur_i, cur_j, cur_head = queue.popleft()
		ground[cur_i][cur_j] = 3
		clean_cnt += 1

		while True:
			if none_cnt == 4:
				none_cnt = 0
				# 2-c
				if cur_head == 0:
					cur_i = cur_i + 1
				if cur_head == 1:
					cur_j = cur_j - 1
				if cur_head == 2:
					cur_i = cur_i - 1
				if cur_head == 3:
					cur_j = cur_j + 1

				if ground[cur_i][cur_j] == 1:
					break

			# north
			if cur_head == 0:
				visit_i = cur_i + west[0]
				visit_j = cur_j + west[1]

				# 2-a
				if ground[visit_i][visit_j] == 0:
					queue.append([visit_i, visit_j, 3])
					break

				# 2-b
				if ground[visit_i][visit_j] == 1 or ground[visit_i][visit_j] == 3:
					cur_head = 3
					none_cnt += 1
					continue

			# east
			if cur_head == 1:
				visit_i = cur_i + north[0]
				visit_j = cur_j + north[1]

				# 2-a
				if ground[visit_i][visit_j] == 0:
					queue.append([visit_i, visit_j, 0])
					break

				# 2-b
				if ground[visit_i][visit_j] == 1 or ground[visit_i][visit_j] == 3:
					cur_head = 0
					none_cnt += 1
					continue

			# south
			if cur_head == 2:
				visit_i = cur_i + east[0]
				visit_j = cur_j + east[1]

				# 2-a
				if ground[visit_i][visit_j] == 0:
					queue.append([visit_i, visit_j, 1])
					break

				# 2-b
				if ground[visit_i][visit_j] == 1 or ground[visit_i][visit_j] == 3:
					cur_head = 1
					none_cnt += 1
					continue

			# west
			if cur_head == 3:
				visit_i = cur_i + south[0]
				visit_j = cur_j + south[1]

				# 2-a
				if ground[visit_i][visit_j] == 0:
					queue.append([visit_i, visit_j, 2])
					break

				# 2-b
				if ground[visit_i][visit_j] == 1 or ground[visit_i][visit_j] == 3:
					cur_head = 2
					none_cnt += 1
					continue

	return clean_cnt


if __name__ == '__main__':
	n, m = map(int, input().split())
	robot_i, robot_j, head = map(int, input().split())
	ground = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(n)]

	print(clean())