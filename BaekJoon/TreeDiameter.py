import sys
from collections import deque


def BFS(graph, start):
	visit = dict()
	output = []
	queue = deque([[start, 0]])

	while queue:
		cur_node, cur_dist = queue.popleft()
		visit[cur_node] = 1
		output.append([cur_node, cur_dist])

		for val in graph[cur_node]:
			visit_node, visit_dist = val
			if visit_node not in visit:
				queue.append([visit_node, cur_dist + visit_dist])
				visit[visit_node] = 1

	output = sorted(output, key=lambda x: x[1])
	return output[-1]


def solution(graph):
	start = BFS(graph, 1)
	end = BFS(graph, start[0])
	print(end[1])


N = int(input())
graph = {i: [] for i in range(1, N + 1)}
for _ in range(N):
	data = sys.stdin.readline().rsplit()
	node = int(data[0])
	edge = data[1:-1]

	for j in range(0, len(edge), 2):
		tmp = [int(edge[j]), int(edge[j + 1])]
		graph[node].append(tmp)

solution(graph)

# 7
# 1 2 1 3 1 -1
# 2 1 1 -1
# 3 1 1 4 3 5 2 -1
# 4 3 3 -1
# 5 3 2 6 3 7 10 -1
# 6 5 3 -1
# 7 5 10 -1