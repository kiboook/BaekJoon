def solution(num):
	dp = [0, 1, 2, 3, 2]

	for i in range(5, num + 1):
		pivot = 1
		tmp = 1_000_000
		while pivot ** 2 <= i:
			if 1 + dp[i - pivot ** 2] < tmp:
				tmp = 1 + dp[i - pivot ** 2]
			pivot += 1
		dp.append(tmp)

	return dp[num]


print(solution(int(input())))