# import sys
#
#
# n = int(input())
# arr = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(n)]
#
# dp = [[0] * 3 for _ in range(n - 1)]
# dp.insert(0, arr[0])
#
# smalldp = [[0] * 3 for _ in range(n - 1)]
# min_dp.insert(0, arr[0])
#
# for i in range(1, n):
# 	first = arr[i][0]
# 	second = arr[i][1]
# 	third = arr[i][2]
#
# 	dp[i][0] = max(dp[i - 1][0] + first, dp[i - 1][1] + first)
# 	dp[i][1] = max(dp[i - 1][0] + second, dp[i - 1][1] + second, dp[i - 1][2] + second)
# 	dp[i][2] = max(dp[i - 1][1] + third, dp[i - 1][2] + third)
#
# 	min_dp[i][0] = min(min_dp[i - 1][0] + first, min_dp[i - 1][1] + first)
# 	min_dp[i][1] = min(min_dp[i - 1][0] + second, min_dp[i - 1][1] + second, min_dp[i - 1][2] + second)
# 	min_dp[i][2] = min(min_dp[i - 1][1] + third, min_dp[i - 1][2] + third)
#
# print(max(dp[n - 1]), min(min_dp[n - 1]))


# import sys
#
#
# n = int(input())
# arr = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(n)]
#
# dp = [[[0, 0]] * 3 for _ in range(n - 1)]
# dp.insert(0, [[i, i] for i in arr[0]])
#
#
# print(dp)
# for i in range(1, n):
# 	first = arr[i][0]
# 	second = arr[i][1]
# 	third = arr[i][2]
#
# 	dp[i][0][0] = max(dp[i - 1][0][0] + first, dp[i - 1][1][0] + first)
# 	dp[i][1][0] = max(dp[i - 1][0][0] + second, dp[i - 1][1][0] + second, dp[i - 1][2][0] + second)
# 	dp[i][2][0] = max(dp[i - 1][1][0] + third, dp[i - 1][2][0] + third)
#
# 	dp[i][0][1] = min(dp[i - 1][0][1] + first, dp[i - 1][1][1] + first)
# 	dp[i][1][1] = min(dp[i - 1][0][1] + second, dp[i - 1][1][1] + second, dp[i - 1][2][1] + second)
# 	dp[i][2][1] = min(dp[i - 1][1][1] + third, dp[i - 1][2][1] + third)
#
# print(dp)


# import sys
#
# n = int(input())
# arr = []
# for _ in range(n):
# 	data = list(map(int, sys.stdin.readline().rsplit()))
# 	arr.append([[i, i] for i in data])
#
# for i in range(1, n):
# 	first = arr[i][0][0]
# 	second = arr[i][1][0]
# 	third = arr[i][2][0]
#
# 	arr[i][0][0] = max(arr[i - 1][0][0] + first, arr[i - 1][1][0] + first)
# 	arr[i][1][0] = max(arr[i - 1][0][0] + second, arr[i - 1][1][0] + second, arr[i - 1][2][0] + second)
# 	arr[i][2][0] = max(arr[i - 1][1][0] + third, arr[i - 1][2][0] + third)
#
# 	arr[i][0][1] = min(arr[i - 1][0][1] + first, arr[i - 1][1][1] + first)
# 	arr[i][1][1] = min(arr[i - 1][0][1] + second, arr[i - 1][1][1] + second, arr[i - 1][2][1] + second)
# 	arr[i][2][1] = min(arr[i - 1][1][1] + third, arr[i - 1][2][1] + third)
#
# print(max(arr[n - 1])[0], min(arr[n - 1])[1])

import sys

n = int(input())
arr = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(n)]
small, large = arr[0], arr[0]

for i in range(1, n):
	large = [max(large[0], large[1]) + arr[i][0],
			 max(large[0], large[1], large[2]) + arr[i][1],
			 max(large[1], large[2]) + arr[i][2]]

	small = [min(small[0], small[1]) + arr[i][0],
			 min(small[0], small[1], small[2]) + arr[i][1],
			 min(small[1], small[2]) + arr[i][2]]

print(max(large), min(small))
