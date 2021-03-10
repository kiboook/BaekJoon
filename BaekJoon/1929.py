from math import sqrt


def solution():
	prime = [True] * (N + 1)
	prime[1] = False

	for i in range(2, int(sqrt(N) + 1)):
		if prime[i]:
			j = 2
			while i * j <= N:
				prime[i * j] = False
				j += 1

	for i in range(M, N + 1):
		if prime[i]:
			print(i)


if __name__ == '__main__':
	M, N = map(int, input().split())

	solution()