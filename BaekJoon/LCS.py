arr1 = input()
arr2 = input()
dp = [[0 for _ in range(len(arr1) + 1)] for _ in range(len(arr2) + 1)]

for i in range(1, len(arr2) + 1):
	for j in range(1, len(arr1) + 1):
		if arr1[j - 1] == arr2[i - 1]:
			dp[i][j] = dp[i - 1][j - 1] + 1
		else:
			dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

for cur in dp:
	print(cur)
print(dp[len(arr2)][len(arr1)])