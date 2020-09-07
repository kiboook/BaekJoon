import sys
from collections import deque


def DFS(graph, start):
	visit = dict()
	stack = [start]

	while stack:
		visit_ver = stack.pop()
		if visit_ver not in visit:
			print(visit_ver, end=' ')
			visit[visit_ver] = 1

		for ver in reversed(graph[visit_ver]):

			if ver not in visit:
				stack.append(ver)


def BFS(graph, start):
	visit = dict()
	queue = deque([start])

	while queue:
		visit_ver = queue.popleft()
		if visit_ver not in visit:
			print(visit_ver, end=' ')
			visit[visit_ver] = 1

		for ver in graph[visit_ver]:
			if ver not in visit:
				queue.append(ver)


N, M, V = map(int, sys.stdin.readline().rsplit())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
	start, end = map(int, sys.stdin.readline().rsplit())
	graph[start].append(end)
	graph[end].append(start)

for i in range(1, N + 1):  # 정점 번호가 작은 순으로 방문해야하기 때문에 정렬한다
	graph[i].sort()

# DFS(graph, V)
print()
BFS(graph, V)

# 5 5
# 1 3
# 1 4
# 4 5
# 4 3
# 3 2