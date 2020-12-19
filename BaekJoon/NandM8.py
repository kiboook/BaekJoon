import sys


def DFS():
	global n, m, data, stack

	if len(stack) == m:
		print(*stack)
		return

	for i in range(n):
		if stack and stack[-1] > data[i]:
			continue

		stack.append(data[i])
		DFS()
		stack.pop()


n, m = map(int, sys.stdin.readline().rsplit())
data = sorted(list(map(int, sys.stdin.readline().rsplit())))
stack = []
DFS()

# import sys
# from itertools import combinations_with_replacement
#
#
# n, m = map(int, sys.stdin.readline().rsplit())
# data = sorted(list(map(int, sys.stdin.readline().rsplit())))
# res = combinations_with_replacement(data, m)
#
# for val in res:
# 	print(*val)