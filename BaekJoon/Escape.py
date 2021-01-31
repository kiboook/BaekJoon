from collections import deque


def solution(water_start, hedgehog_start):
	water_queue = deque(water_start)
	hedgehog_queue = deque([hedgehog_start])
	dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

	while hedgehog_queue:
		hedgehog_i, hedgehog_j, hedgehog_minute = hedgehog_queue.popleft()
		while water_queue:
			if water_queue[0][2] == hedgehog_minute:
				water_i, water_j, water_minute = water_queue.popleft()
			else:
				break
			for val in dirs:
				water_visit_i = water_i + val[0]
				water_visit_j = water_j + val[1]
				if 0 <= water_visit_i < r and 0 <= water_visit_j < c:
					if ground[water_visit_i][water_visit_j] == '.':
						ground[water_visit_i][water_visit_j] = 'X'
						water_queue.append([water_visit_i, water_visit_j, water_minute + 1])

		for val in dirs:
			hedgehog_visit_i = hedgehog_i + val[0]
			hedgehog_visit_j = hedgehog_j + val[1]
			if 0 <= hedgehog_visit_i < r and 0 <= hedgehog_visit_j < c:
				if ground[hedgehog_visit_i][hedgehog_visit_j] == '.':
					ground[hedgehog_visit_i][hedgehog_visit_j] = 'X'
					hedgehog_queue.append([hedgehog_visit_i, hedgehog_visit_j, hedgehog_minute + 1])
				if ground[hedgehog_visit_i][hedgehog_visit_j] == 'D':
					return hedgehog_minute + 1

	return "KAKTUS"


if __name__ == '__main__':
	r, c = map(int, input().rsplit())
	ground = [list(map(str, input())) for _ in range(r)]

	water_start = []
	hedgehog_start = []
	for i in range(r):
		for j in range(c):
			if ground[i][j] == '*':
				water_start.append([i, j, 0])
			if ground[i][j] == 'S':
				hedgehog_start = [i, j, 0]

	print(solution(water_start, hedgehog_start))