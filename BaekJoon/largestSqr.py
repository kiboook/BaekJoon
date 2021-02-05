def solution():
	global arr
	up = [-1, 0]
	left = [0, -1]
	left_up = [-1, -1]

	for i in range(1, n):
		for j in range(1, m):
			up_val = arr[i + up[0]][j + up[1]]
			left_val = arr[i + left[0]][j + left[1]]
			left_up_val = arr[i + left_up[0]][j + left_up[1]]
			if 0 < up_val and 0 < left_val and 0 < left_up_val and 0 < arr[i][j]:
				arr[i][j] = (int(min(up_val, left_val, left_up_val) ** 0.5) + 1) ** 2

	return max(sum(arr, []))


if __name__ == '__main__':
	n, m = map(int, input().split())
	arr = [list(map(int, input())) for _ in range(n)]

	print(solution())
