import sys


def make_max(arr):
	result = 0
	a, b = [[0, 1], [0, 2], [0, 3]], [[1, 0], [2, 0], [3, 0]]
	c = [[0, 1], [1, 0], [1, 1]]
	d, e = [[1, 0], [2, 0], [2, 1]], [[0, 1], [0, 2], [-1, 2]]
	f, g = [[0, 1], [1, 1], [2, 1]], [[0, 1], [0, 2], [1, 0]]
	h, i = [[1, 0], [1, 1], [2, 1]], [[0, 1], [-1, 1], [-1, 2]]
	j, k = [[1, 0], [1, -1], [1, 1]], [[-1, 0], [0, 1], [1, 0]]
	l, m = [[0, -1], [-1, 0], [1, 0]], [[0, -1], [1, 0], [0, 1]]
	n, o = [[0, 1], [-1, 1], [-2, 1]], [[0, 1], [0, 2], [1, 2]]
	p, q = [[0, 1], [1, 0], [2, 0]], [[1, 0], [1, 1], [1, 2]]
	r, s = [[1, 0], [1, -1], [2, -1]], [[0, 1], [1, 1], [1, 2]]
	move = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s]

	for i in range(N):
		for j in range(M):
			for cur in move:
				tmp = arr[i][j]
				for val in cur:
					move_i, move_j = i + val[0], j + val[1]
					if 0 <= move_i < N and 0 <= move_j < M:
						tmp += arr[move_i][move_j]

				if result < tmp:
					result = tmp

	return result


N, M = map(int, input().split())

my_arr = []
for _ in range(N):
	my_arr.append(list(map(int, sys.stdin.readline().rsplit())))

print(make_max(my_arr))
