import sys
from collections import deque


def BFS():
	queue = deque([1])
	visit = {}

	while queue:
		parent = queue.popleft()
		visit[parent] = 1

		for child in graph[parent]:
			if child not in visit:
				res[child] = parent
				queue.append(child)
				visit[child] = 1


n = int(input())
data = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(n - 1)]
graph = {i: [] for i in range(1, n + 1)}
res = {i: 0 for i in range(2, n + 1)}

for val in data:
	graph[val[0]].append(val[1])
	graph[val[1]].append(val[0])

BFS()
for val in res.values():
	print(val)