import sys
import heapq


def solution(graph, start, end, node_num):
	dist = {i + 1: INF for i in range(node_num)}
	dist[start] = 0
	queue = []
	heapq.heappush(queue, [dist[start], start])
	while queue:
		cur_cost, cur_node = heapq.heappop(queue)

		if dist[cur_node] < cur_cost:
			continue

		for val in graph[cur_node]:
			visit_cost, visit_node = val
			if dist[visit_node] > visit_cost + cur_cost:
				dist[visit_node] = visit_cost + cur_cost
				heapq.heappush(queue, [dist[visit_node], visit_node])

	print(dist[end])


INF = 200_000_000
node_num = int(input())
edge_num = int(input())
graph = {i + 1: [] for i in range(node_num)}

for _ in range(edge_num):
	start, end, cost = map(int, sys.stdin.readline().rsplit())
	graph[start].append([cost, end])

start, end = map(int, input().split())
solution(graph, start, end, node_num)