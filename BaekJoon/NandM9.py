import sys
from collections import Counter


def DFS():
	if len(stack) == m:
		print(*stack)
		return

	for i in range(len(data)):
		if stack and data[i] in stack and data[i] not in duplicate:
			continue
		if data[i] in duplicate and count[data[i]] < Counter(stack)[data[i]] + 1:
			continue
		stack.append(data[i])
		DFS()
		stack.pop()


n, m = map(int, sys.stdin.readline().rsplit())
data = list(map(int, sys.stdin.readline().rsplit()))
count = Counter(data)
stack = []
duplicate = []

for key, value in zip(count.keys(), count.values()):
	if value > 1:
		duplicate.append(key)
data = sorted(list(set(data)))

DFS()

# import sys
# from itertools import permutations
#
#
# n, m = map(int, sys.stdin.readline().rsplit())
# data = map(int, sys.stdin.readline().rsplit())
#
# for val in sorted(list(set(permutations(data, m)))):
# 	print(*val)