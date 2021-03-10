import sys


def up(data):
	dp = [1 for _ in range(n)]

	for i in range(n):
		for j in range(i):
			if data[i] > data[j]:
				dp[i] = max(dp[i], dp[j] + 1)

	return dp


def down(data):
	dp = [1 for _ in range(n)]

	for i in range(n, -1, -1):
		for j in range(i, n):
			if data[i] > data[j]:
				dp[i] = max(dp[i], dp[j] + 1)

	return dp


def solution():
	up_dp = up(arr)
	down_dp = list(reversed(up(arr[::-1])))

	answer = [i + j - 1 for i, j in zip(up_dp, down_dp)]
	return max(answer)


if __name__ == "__main__":
	n = int(input())
	arr = list(map(int, sys.stdin.readline().rsplit()))

	print(solution())