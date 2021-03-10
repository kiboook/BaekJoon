def solution():
	dp = [data[0]]
	for i in range(n - 1):
		dp.append(max(dp[i] + data[i + 1], data[i + 1]))

	return max(dp)


if __name__ == "__main__":
	n = int(input())
	data = list(map(int, input().split()))

	print(solution())