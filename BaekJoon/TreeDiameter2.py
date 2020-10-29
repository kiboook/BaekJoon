import sys
from collections import deque


def BFS(graph, start):
	queue = deque([[start, 0]])
	visit = dict()
	dist = list()
	visit[start] = 1

	while queue:
		cur_node, cur_weight = queue.popleft()
		dist.append([cur_node, cur_weight])

		for val in graph[cur_node]:
			visit_node, visit_weight = val
			if visit_node not in visit:
				visit[visit_node] = 1
				queue.append([visit_node, cur_weight + visit_weight])

	return sorted(dist, key=lambda x: x[1])[-1]


node_num = int(input())
graph = {i + 1: [] for i in range(node_num)}

for _ in range(node_num - 1):
	parent, child, weight = map(int, sys.stdin.readline().rsplit())
	graph[parent].append([child, weight])
	graph[child].append([parent, weight])

temp = BFS(graph, 1)
print(BFS(graph, temp[0])[1])