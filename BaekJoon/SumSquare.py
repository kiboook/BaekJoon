if __name__ == '__main__':
	area = 0
	visit = [[0] * 101 for _ in range(101)]
	data = [list(map(int, input().rsplit())) for _ in range(4)]

	for square_coord in data:
		left_x, left_y, right_x, right_y = square_coord

		for x in range(left_x, right_x):
			for y in range(left_y, right_y):
				visit[x][y] = 1

	print(sum(sum(visit, [])))