import sys


def Floyd(graph):
	for k in range(N):
		for i in range(N):
			for j in range(N):
				if graph[i][j] == 0:
					graph[i][j] = INF

				graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


INF = 1_000_000
N = int(input())
in_graph = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)]
Floyd(in_graph)

for i in range(N):
	for j in range(N):
		if in_graph[i][j] != INF:
			in_graph[i][j] = 1
		else:
			in_graph[i][j] = 0

for val in in_graph:
	val = map(str, val)
	print(' '.join(val))