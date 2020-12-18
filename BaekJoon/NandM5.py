# import sys
# from itertools import permutations
#
#
# n, m = map(int, sys.stdin.readline().rsplit())
# data = sorted(list(map(int, sys.stdin.readline().rsplit())))
# res = permutations(data, m)
#
# for val in res:
# 	print(*val)

import sys


def DFS():
	global n, m, data, stack

	if len(stack) == m:
		print(*stack)
		return

	for i in range(n):
		stack.append(data[i])

		if len(set(stack)) != len(stack):
			stack.pop()
		else:
			DFS()
			stack.pop()


n, m = map(int, sys.stdin.readline().rsplit())
data = sorted(list(map(int, sys.stdin.readline().rsplit())))
stack = []
DFS()
