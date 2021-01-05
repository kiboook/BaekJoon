import sys


def air_conditional():
	top = fresh_index[0]

	# 오른쪽 바람
	right_tmp = arr[top[0]][c - 1]
	for i in range(c - 1, 1, -1):
		arr[top[0]][i] = arr[top[0]][i - 1]
	arr[top[0]][top[1] + 1] = 0

	# 위쪽 바람
	top_tmp = arr[0][c - 1]
	for i in range(top[0] - 1):
		arr[i][c - 1] = arr[i + 1][c - 1]
	arr[top[0] - 1][c - 1] = right_tmp

	# 왼쪽 바람
	left_tmp = arr[0][0]
	for i in range(c - 1):
		arr[0][i] = arr[0][i + 1]
	arr[0][c - 2] = top_tmp

	# 아래쪽 바람
	for i in range(top[0] - 1, 1, -1):
		arr[i][0] = arr[i - 1][0]
	arr[1][0] = left_tmp

	bottom = fresh_index[1]

	# 오른쪽 바람
	right_tmp = arr[bottom[0]][c - 1]
	for i in range(c - 1, 1, -1):
		arr[bottom[0]][i] = arr[bottom[0]][i - 1]
	arr[bottom[0]][bottom[1] + 1] = 0

	# 아래쪽 바람
	bottom_tmp = arr[r - 1][c - 1]
	for i in range(r - 1, bottom[0] + 1, - 1):
		arr[i][c - 1] = arr[i - 1][c - 1]
	arr[bottom[0] + 1][c - 1] = right_tmp

	# 왼쪽 바람
	left_tmp = arr[r - 1][0]
	for i in range(c - 1):
		arr[r - 1][i] = arr[r - 1][i + 1]
	arr[r - 1][c - 2] = bottom_tmp

	# 위쪽 바람
	for i in range(bottom[0] + 1, r - 2):
		arr[i][0] = arr[i + 1][0]
	arr[r - 2][0] = left_tmp

	arr[top[0]][top[1]] = -1
	arr[bottom[0]][bottom[1]] = -1
	return


def sum_dust(arr, tmp_arr):
	return [[arr[i][j] + tmp_arr[i][j] for j in range(c)] for i in range(r)]


def dust():
	global arr

	tmp_arr = [[0] * c for _ in range(r)]
	visit = [[-1, 0], [0, 1], [1, 0], [0, -1]]

	for i in range(r):
		for j in range(c):
			if arr[i][j] > 0:
				# 먼지 확산
				spread_area = 0
				spread_dust = arr[i][j] // 5
				for cur in visit:
					visit_i = cur[0] + i
					visit_j = cur[1] + j
					if 0 <= visit_i < r and 0 <= visit_j < c and [visit_i, visit_j] not in fresh_index:
						tmp_arr[visit_i][visit_j] += spread_dust
						spread_area += 1

				arr[i][j] = arr[i][j] - (spread_dust * spread_area)

	arr = sum_dust(arr, tmp_arr)
	air_conditional()
	return


if __name__ == '__main__':
	res = 0
	r, c, t = map(int, input().split())
	arr = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(r)]

	fresh_index = []
	for i in range(r):
		for j in range(c):
			if arr[i][j] == -1:
				fresh_index.append([i, j])

	for _ in range(t):
		dust()

	print(sum(sum(arr, [])) + 2)

