import sys


def check_paper(width, x, y):
	pivot = arr[x][y]
	for i in range(x, x + width):
		for j in range(y, y + width):
			if arr[i][j] != pivot:
				return [False, -1]
	return [True, pivot]


def make_paper(width, i, j):
	check = check_paper(width, i, j)
	if check[0]:
		count[check[1]] += 1
		return

	else:
		make_paper(width // 2, i, j)
		make_paper(width // 2, i, j + width // 2)
		make_paper(width // 2, i + width // 2, j)
		make_paper(width // 2, i + width // 2, j + width // 2)


N = int(input())
arr = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)]
count = {0: 0, 1: 0}
make_paper(N, 0, 0)

for val in count.values():
	print(val)