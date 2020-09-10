from collections import deque


def BFS(graph, start, goal):
	visited = dict()
	queue = deque([[start, 0]])

	while queue:
		visit_ver = queue.popleft()
		visited[visit_ver[0]] = 1

		if visit_ver[0] == goal:
			return visit_ver[1]

		for ver in graph[visit_ver[0]]:
			if ver not in visited:
				queue.append([ver, visit_ver[1] + 1])
				visited[ver] = 1


def find_min_time(N, K):
	if N >= K:
		return N - K

	graph = {i: [] for i in range(0, 100001)}
	graph[0] = [1]
	graph[1] = [0, 2]

	for i in range(2, 100001):
		tmp = [i - 1]
		if i + 1 <= 100000:
			tmp.append(i + 1)
		if i * 2 <= 100000:
			tmp.append(i * 2)
		graph[i] = tmp

	return BFS(graph, N, K)


N, K = map(int, input().split())
print(find_min_time(N, K))