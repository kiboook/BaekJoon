# import sys
#
#
# n, m = map(int, sys.stdin.readline().rsplit())
# arr = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(n)]
# loc = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(m)]
# prefixSum = [[0 for _ in range(n)] for _ in range(n)]
#
# for i in range(n):
# 	prefixSum[i][0] = arr[i][0]
#
# for i in range(n):
# 	for j in range(1, n):
# 		prefixSum[i][j] = prefixSum[i][j - 1] + arr[i][j]
#
# for cur in loc:
# 	res = 0
# 	x1, y1, x2, y2 = cur
# 	if y1 == 1:
# 		for i in range(x1 - 1, x2):
# 			res += prefixSum[i][y2 - 1]
#
# 	else:
# 		for i in range(x1 - 1, x2):
# 			res += (prefixSum[i][y2 - 1] - prefixSum[i][y1 - 2])
# 	print(res)

import sys

n, m = map(int, sys.stdin.readline().rsplit())
arr = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(n)]
loc = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(m)]
prefixSum = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
	prefixSum[i][0] = arr[i][0]

for i in range(n):
	for j in range(1, n):
		prefixSum[i][j] = prefixSum[i][j - 1] + arr[i][j]

for i in range(n):
	for j in range(1, n):
		prefixSum[j][i] = prefixSum[j - 1][i] + prefixSum[j][i]

for cur in loc:
	x1, y1, x2, y2 = cur

	if x1 == 1 and y1 == 1:
		print(prefixSum[x2 - 1][y2 - 1])
	elif x1 == 1:
		print(prefixSum[x2 - 1][y2 - 1] - prefixSum[x2 - 1][y1 - 2])
	elif y1 == 1:
		print(prefixSum[x2 - 1][y2 - 1] - prefixSum[x1 - 2][y2 - 1])
	else:
		print(prefixSum[x2 - 1][y2 - 1] - prefixSum[x2 - 1][y1 - 2] - prefixSum[x1 - 2][y2 - 1] + prefixSum[x1 - 2][y1 - 2])