import sys


n = int(input())
data = list(map(int, sys.stdin.readline().rsplit()))
dp = [0 for i in range(n)]
dp[0] = 1

for i in range(1, len(data)):
	for j in range(i):
		if data[i] > data[j] and dp[i] < dp[j]:
			dp[i] = dp[j]
	dp[i] += 1

print(max(dp))

# 8
# 1 5 10 3 13 18 15 16