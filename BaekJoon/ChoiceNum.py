from collections import deque


def DFS(start):
	global res
	queue = deque([start])
	visit = {start: 1}
	route = [start]

	while queue:
		visit_node = graph[queue.popleft()]
		if visit_node == start:
			res = res + route
			return

		route.append(visit_node)
		if visit_node not in visit:
			queue.append(visit_node)
			visit[visit_node] = 1

	return


if __name__ == '__main__':
	n = int(input())
	graph = {i + 1: int(input()) for i in range(n)}

	res = []
	for node in graph:
		DFS(node)

	res = sorted(list(set(res)))
	print(len(res))
	for val in res:
		print(val)