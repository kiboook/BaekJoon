import sys


def DFS(index):
	global n, m, data, stack

	if len(stack) == m:
		print(*stack)
		return

	for i in range(index, n):
		if stack and data[i] < stack[-1]:
			continue
		stack.append(data[i])
		DFS(0)
		stack.pop()


n, m = map(int, sys.stdin.readline().rsplit())
data = [i for i in range(1, n + 1)]
stack = []
DFS(0)