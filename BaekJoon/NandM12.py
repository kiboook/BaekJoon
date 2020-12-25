import sys


def DFS():
	if len(stack) == m:
		print(*stack)
		return

	for i in range(len(data)):
		if stack and stack[-1] > data[i]:
			continue

		stack.append(data[i])
		DFS()
		stack.pop()


n, m = map(int, sys.stdin.readline().rsplit())
data = sorted(list(set(map(int, sys.stdin.readline().rsplit()))))
stack = []
DFS()


# import sys
# from itertools import combinations_with_replacement
#
#
# n, m = map(int, sys.stdin.readline().rsplit())
# data = sorted(list(set(map(int, sys.stdin.readline().rsplit()))))
#
# for val in combinations_with_replacement(data, m):
# 	print(*val)