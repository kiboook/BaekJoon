import sys
import heapq


INF = 2_000_000


def dijkstra(graph, start, end):
	dist = {i + 1: INF for i in range(len(graph))}
	dist[start] = 0
	queue = []
	heapq.heappush(queue, [dist[start], start])

	while queue:
		cur_weight, cur_node = heapq.heappop(queue)
		if cur_weight > dist[cur_node]:
			continue

		for val in graph[cur_node]:
			visit_weight, visit_node = val[0], val[1]
			if visit_weight + cur_weight <= dist[visit_node]:
				dist[visit_node] = visit_weight + cur_weight
				heapq.heappush(queue, [dist[visit_node], visit_node])

	return dist[end]


town_cnt, road_cnt, goal = map(int, input().split())
graph = {i + 1: [] for i in range(town_cnt)}

for _ in range(road_cnt):
	start, end, weight = map(int, sys.stdin.readline().rsplit())
	graph[start].append([weight, end])

answer = 0
for node in range(1, town_cnt + 1):
	temp = 0
	if node == goal:
		pass
	else:
		temp += dijkstra(graph, node, goal)
		temp += dijkstra(graph, goal, node)

	if temp >= answer:
		answer = temp

print(answer)

