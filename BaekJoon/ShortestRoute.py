import sys
import heapq


def solution(graph, start, node_num):
	dist = {i + 1: 5_000_000 for i in range(node_num)}
	dist[start] = 0
	queue = []
	heapq.heappush(queue, [dist[start], start])

	while queue:
		cur_dist, cur_node = heapq.heappop(queue)

		if dist[cur_node] < cur_dist:
			continue

		for val in graph[cur_node]:
			weight, visit_node = val

			if dist[visit_node] > weight + cur_dist:
				dist[visit_node] = weight + cur_dist
				heapq.heappush(queue, [weight + cur_dist, visit_node])

	for val in dist.items():
		if val[1] == 5_000_000:
			print("INF")
		else:
			print(val[1])


node_num, edge_num = map(int, input().split())
pivot = int(input())
graph = {i + 1: [] for i in range(node_num)}

for _ in range(edge_num):
	start, end, weight = map(int, sys.stdin.readline().rsplit())
	graph[start].append([weight, end])

solution(graph, pivot, node_num)