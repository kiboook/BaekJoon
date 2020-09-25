import sys
from collections import deque


def calculateDistance(start, end):
	return abs(start[0] - end[0]) + abs(start[1] - end[1])


def makeGraph(coordinates):
	coord_len = len(coordinates)
	graph = {i: [] for i in range(coord_len)}

	for i in range(coord_len):
		for j in range(coord_len):
			if i != j and calculateDistance(coordinates[i], coordinates[j]) <= 1000:
				graph[i].append(j)

	return graph


def BFS(graph, coordinates):
	queue = deque([0])
	visit = {0: 1}

	while queue:
		cur_node = queue.popleft()
		for val in graph[cur_node]:
			if val not in visit:
				if coordinates[val] == coordinates[-1]:
					return 'happy'

				visit[val] = 1
				queue.append(val)
	return 'sad'


for _ in range(int(input())):
	coordinates = []

	for _ in range(int(input()) + 2):
		coord = list(map(int, sys.stdin.readline().rsplit()))
		coordinates.append(coord)

	graph = makeGraph(coordinates)
	print(BFS(graph, coordinates))