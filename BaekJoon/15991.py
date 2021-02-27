import sys
from collections import deque


def BFS(N, graph, k, start):
	visit = [False] * (N + 1)
	queue = deque([[start, float('inf')]])
	visit[start] = True

	answer = 0
	while queue:
		node, USADO = queue.popleft()
		for i in graph[node]:
			visit_node, visit_USADO = i

			min_USADO = min(USADO, visit_USADO)
			if not visit[visit_node] and min_USADO >= k:
				answer += 1
				visit[visit_node] = True
				queue.append([visit_node, min_USADO])

	return answer


if __name__ == "__main__":
	N, Q = map(int, input().split())
	graph = {i + 1: [] for i in range(N)}

	for _ in range(N - 1):
		start, end, USADO = map(int, sys.stdin.readline().rsplit())
		graph[start].append([end, USADO])
		graph[end].append([start, USADO])

	for _ in range(Q):
		k, check = map(int, sys.stdin.readline().rsplit())
		print(BFS(N, graph, k, check))