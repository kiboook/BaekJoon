import sys


def find_max_score(stairs):
	if len(stairs) == 1:
		return stairs[0]

	if len(stairs) == 2:
		return stairs[0] + stairs[1]

	if len(stairs) == 3:
		return max(stairs[0] + stairs[2], stairs[1] + stairs[2])

	dp = list()
	dp.append(stairs[0])
	dp.append(stairs[0] + stairs[1])
	dp.append(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))

	for i in range(3, len(stairs)):
		dp.append(max(stairs[i] + stairs[i - 1] + dp[i - 3], stairs[i] + dp[i - 2]))

	return dp[-1]


N = int(input())
_stairs = [int(sys.stdin.readline().rsplit()[0]) for _ in range(N)]
print(find_max_score(_stairs))