from sys import stdin
import heapq


def dijkstra(graph, start, end):
	dist = {i + 1: float('inf') for i in range(len(graph))}
	dist[start] = 0
	heap = list()
	heapq.heappush(heap, (0, start))
	while heap:
		cur_dist, cur_node = heapq.heappop(heap)

		if dist[cur_node] < cur_dist:
			continue
		for cur in graph[cur_node]:
			visit_node, edge_dist = cur

			if cur_dist + edge_dist < dist[visit_node]:
				dist[visit_node] = cur_dist + edge_dist
				heapq.heappush(heap, (cur_dist + edge_dist, visit_node))

	return dist[end]


def solution(N, E):
	graph = {i: [] for i in range(1, N + 1)}
	for _ in range(E):
		start, end, dist = map(int, stdin.readline().rsplit())
		graph[start].append((end, dist))
		graph[end].append((start, dist))

	v1, v2 = map(int, input().split())
	first_v1 = dijkstra(graph, 1, v1) + dijkstra(graph, v1, v2) + dijkstra(graph, v2, N)
	first_v2 = dijkstra(graph, 1, v2) + dijkstra(graph, v2, v1) + dijkstra(graph, v1, N)

	answer = min(first_v1, first_v2)
	return -1 if answer == float('inf') else answer


if __name__ == "__main__":
	N, E = map(int, input().split())
	print(solution(N, E))