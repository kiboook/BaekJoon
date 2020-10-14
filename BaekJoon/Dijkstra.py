import sys
import heapq


def dijkstra(graph, start, end):
	dist = {i + 1: 1_000_000 for i in range(node_num)}
	dist[start] = 0
	queue = []
	heapq.heappush(queue, [dist[start], start])

	while queue:
		cur_dist, cur_node = heapq.heappop(queue)

		if dist[cur_node] < cur_dist:
			continue

		for cur in graph[cur_node]:
			weight, visit_node = cur

			if weight + cur_dist < dist[visit_node]:
				dist[visit_node] = weight + cur_dist
				heapq.heappush(queue, [weight + cur_dist, visit_node])

	return dist[end]


def solution(graph, v1, v2):
	first_v1 = dijkstra(graph, 1, v1) + dijkstra(graph, v1, v2) + dijkstra(graph, v2, node_num)
	first_v2 = dijkstra(graph, 1, v2) + dijkstra(graph, v2, v1) + dijkstra(graph, v1, node_num)

	answer = min(first_v1, first_v2)
	if answer >= 1_000_000:
		print(-1)
	else:
		print(answer)


node_num, edge_num = map(int, input().split())
graph = {i + 1: [] for i in range(node_num)}

for _ in range(edge_num):
	start, end, dist = map(int, sys.stdin.readline().rsplit())
	graph[start].append([dist, end])
	graph[end].append([dist, start])

v1, v2 = map(int, input().split())

solution(graph, v1, v2)