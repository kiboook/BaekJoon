def solution():
	dp = [1] * n

	for i in range(1, n):
		for j in range(i):
			if arr[i] < arr[j]:
				dp[i] = max(dp[i], dp[j] + 1)

	return n - max(dp)


if __name__ == '__main__':
	n = int(input())
	arr = list(map(int, input().split()))
	print(solution())