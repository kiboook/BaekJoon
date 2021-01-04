import sys


def find_route(i, j, state):
	global res

	if i == j == home_size - 1:
		res += 1

	if state == 0 or state == 1 or state == 2:
		if i + 1 < home_size and j + 1 < home_size:
			if home[i][j + 1] == home[i + 1][j] == home[i + 1][j + 1] == 0:
				find_route(i + 1, j + 1, 2)

	if state == 0 or state == 2:
		if j + 1 < home_size and home[i][j + 1] != 1:
			find_route(i, j + 1, 0)

	if state == 1 or state == 2:
		if i + 1 < home_size and home[i + 1][j] != 1:
			find_route(i + 1, j, 1)


if __name__ == '__main__':
	home_size = int(input())
	home = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(home_size)]
	res = 0

	find_route(0, 1, 0)
	print(res)