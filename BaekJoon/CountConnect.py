import sys
from collections import deque


def BFS(graph, start, visited):
	queue = deque([start])

	while queue:
		cur_ver = queue.popleft()
		visited[start] = 1

		for ver in graph[cur_ver]:
			if ver not in visited:
				queue.append(ver)
				visited[start] = 1


def count_connect(graph, visited):
	count = 0

	for ver, connect_list in graph.items():
		if ver not in visited:
			BFS(graph, ver, visited)
			count += 1

	return count


N, M = map(int, sys.stdin.readline().rsplit())
graph = {i: [] for i in range(1, N + 1)}
visited = {}

for _ in range(M):
	start, end = map(int, sys.stdin.readline().rsplit())

	graph[start].append(end)
	graph[end].append(start)

print(count_connect(graph, visited))
