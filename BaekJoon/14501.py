import sys


def solution():
	dp = [0 for _ in range(n + 1)]

	for i in range(n, -1, -1):
		if i + t[i] > n + 1:
			continue
		else:
			try:
				dp[i] = p[i] + max(dp[i + t[i]:])
			except ValueError:
				dp[i] = p[i]
	print(dp)
	return max(dp)


if __name__ == "__main__":
	n = int(input())
	t, p = [0], [0]

	for _ in range(n):
		time, cost = map(int, sys.stdin.readline().rsplit())
		t.append(time)
		p.append(cost)

	print(solution())