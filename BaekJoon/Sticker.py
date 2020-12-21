import sys


def findMaxStickerScore(arr):
	data = arr
	global n

	if n == 1:
		return max(data[0][0], data[1][0])
	elif n == 2:
		return max(data[0][0] + data[1][1], data[1][0] + data[0][1])

	data[0][1] = data[1][0] + data[0][1]
	data[1][1] = data[0][0] + data[1][1]
	for j in range(2, n):
		data[0][j] = max(data[0][j] + data[1][j - 1], data[0][j] + data[1][j - 2])
		data[1][j] = max(data[1][j] + data[0][j - 1], data[1][j] + data[0][j - 2])

	return max(data[0][n - 1], data[1][n - 1])


testCase = int(input())
for _ in range(testCase):
	n = int(input())
	dp = []
	for _ in range(2):
		dp.append(list(map(int, sys.stdin.readline().rsplit())))
	print(findMaxStickerScore(dp))