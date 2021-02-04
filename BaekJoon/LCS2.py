def solution():
	len_fisrt = len(first)
	len_second = len(second)
	dp = [[''] * (len_fisrt + 1) for _ in range(len_second + 1)]

	for i in range(1, len_second + 1):
		for j in range(1, len_fisrt + 1):
			if second[i - 1] == first[j - 1]:
				dp[i][j] = dp[i - 1][j - 1] + second[i - 1]
			else:
				if len(dp[i - 1][j]) < len(dp[i][j - 1]):
					dp[i][j] = dp[i][j - 1]
				else:
					dp[i][j] = dp[i - 1][j]

	print(len(dp[len_second][len_fisrt]))
	print(dp[len_second][len_fisrt])
	return


if __name__ == '__main__':
	first = input()
	second = input()

	solution()