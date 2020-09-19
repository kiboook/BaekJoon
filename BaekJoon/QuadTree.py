import sys


def check_arr(width, x, y):

	pivot = arr[x][y]
	for i in range(x, x + width):
		for j in range(y, y + width):
			if pivot != arr[i][j]:
				return [False, -1]
	return [True, pivot]


def do_egg(width, i, j):
	global answer

	check = check_arr(width, i, j)
	if check[0]:
		print(check[1], end='')
		return
	else:
		print('(', end='')
		do_egg(width // 2, i, j)
		do_egg(width // 2, i, j + width // 2)
		do_egg(width // 2, i + width // 2, j)
		do_egg(width // 2, i + width // 2, j + width // 2)
		print(')', end='')


N = int(input())
arr = [[int(x) for x in sys.stdin.readline().rsplit()[0]] for _ in range(N)]
do_egg(N, 0, 0)

# 8
# 00000000
# 00000000
# 00001111
# 00001111
# 00011111
# 00111111
# 00111111
# 00111111