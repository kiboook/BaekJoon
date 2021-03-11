import sys


def solution():
	max_cost = 0
	dp = [0 for _ in range(n + 1)]

	for i in range(n - 1, -1, -1):
		if t[i] + i <= n:
			dp[i] = max(max_cost, dp[t[i] + i] + p[i])
			max_cost = dp[i]
		else:
			dp[i] = max_cost
	print(dp)
	return max_cost


if __name__ == "__main__":
	n = int(input())
	t, p = [], []

	for _ in range(n):
		time, cost = map(int, sys.stdin.readline().rsplit())
		t.append(time)
		p.append(cost)

	print(solution())