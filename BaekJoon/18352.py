import sys
import heapq


def dijkstra(graph, start, N):
	distance = [float('inf')] * (N + 1)
	distance[start] = 0
	queue = []
	heapq.heappush(queue, [0, start])

	while queue:
		dist, now = heapq.heappop(queue)
		if distance[now] < dist:
			continue

		for i in graph[now]:
			cost = dist + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(queue, [cost, i[0]])

	return distance


def solution(N, M, K, X):
	graph = {i + 1: [] for i in range(N)}
	for _ in range(M):
		start, end = map(int, sys.stdin.readline().rsplit())
		graph[start].append([end, 1])

	dists = dijkstra(graph, X, N)
	no_answer = True
	for idx, dist in enumerate(dists):
		if dist == K:
			no_answer = False
			print(idx)

	if no_answer:
		print(-1)


if __name__ == '__main__':
	N, M, K, X = map(int, input().split())
	solution(N, M, K, X)