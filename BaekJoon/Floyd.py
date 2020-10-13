import sys


def solution(graph, node_num):
	for k in range(node_num):
		for i in range(node_num):
			for j in range(node_num):
				graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

	for i in range(node_num):
		for j in range(node_num):
			if i == j or graph[i][j] == 100_000_000:
				print(0, end=' ')
			else:
				print(graph[i][j], end=' ')
		print()


node_num = int(input())
edge_num = int(input())
graph = [[100_000_000] * node_num for _ in range(node_num)]

for _ in range(edge_num):
	start, end, dist = map(int, sys.stdin.readline().rsplit())

	start_to_end_dist = graph[start - 1][end - 1]
	if start_to_end_dist > dist:
		graph[start - 1][end - 1] = dist

solution(graph, node_num)