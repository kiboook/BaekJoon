from collections import deque
import sys


def find_virus_com(graph):
	virus = -1
	queue = deque([1])
	visited = dict()

	while queue:
		cur_com = queue.popleft()
		visited[cur_com] = 1
		virus += 1

		for com in _graph[cur_com]:
			if com not in visited:
				visited[com] = 1
				queue.append(com)

	return virus


computer_num = int(input())
route_num = int(input())

_graph = {i: [] for i in range(1, computer_num + 1)}
for _ in range(route_num):
	start, end = map(int, sys.stdin.readline().rsplit())
	_graph[start].append(end)
	_graph[end].append(start)

print(find_virus_com(_graph))
