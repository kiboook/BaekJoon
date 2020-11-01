import sys
from copy import deepcopy


size = int(input())
arr = []
dp = []
for _ in range(size):
	tmp = list(map(int, sys.stdin.readline().rsplit()))
	arr.append(tmp)

dp = deepcopy(arr)
for i in range(size - 1):
	for j in range(i + 1):
		left = dp[i][j] + arr[i + 1][j]
		right = dp[i][j] + arr[i + 1][j + 1]

		dp[i + 1][j] = max(dp[i + 1][j], left)
		dp[i + 1][j + 1] = max(dp[i + 1][j + 1], right)

print(max(sum(dp, [])))