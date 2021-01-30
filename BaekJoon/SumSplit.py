def solution():
	dp = [[1] * (K + 1) for _ in range(N + 1)]
	for i in range(N + 1):
		dp[i][0] = 0

	for i in range(1, N + 1):
		for j in range(2, K + 1):
			sum = 0
			for n in range(i + 1):
				sum += dp[n][j - 1]
			dp[i][j] = sum

	return dp[N][K] % 1_000_000_000


if __name__ == '__main__':
	N, K = map(int, input().rsplit())
	print(solution())