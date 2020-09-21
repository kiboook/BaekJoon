import sys
from math import gcd


def find_LMC(M, N):
	_gcd = gcd(M, N)
	return _gcd * (M // _gcd) * (N // _gcd)


def find_kaing(M, N, x, y):
	if M < N:
		M, N = N, M
		x, y = y, x

	start = x % N
	if start == 0:
		start = N

	cnt = 0
	while start != y:
		start += M - N
		start %= N
		if start == 0:
			start = N
		cnt += 1

		if M * cnt > find_LMC(M, N):
			return -1

	return M * cnt + x


T = int(input())
for _ in range(T):
	in_M, in_N, in_x, in_y = map(int, sys.stdin.readline().rsplit())
	print(find_kaing(in_M, in_N, in_x, in_y))
