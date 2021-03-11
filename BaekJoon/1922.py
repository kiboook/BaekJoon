import sys


def find_parent(parent, node):
	if parent[node] != node:
		parent[node] = find_parent(parent, parent[node])

	return parent[node]


def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b


def solution():
	answer = 0
	parent = [i for i in range(node_cnt + 1)]
	edges.sort()

	for edge in edges:
		cost, a, b = edge
		if find_parent(parent, a) != find_parent(parent, b):
			union_parent(parent, a, b)
			answer += cost

	return answer


if __name__ == "__main__":
	node_cnt = int(input())
	edge_cnt = int(input())
	edges = []
	for _ in range(edge_cnt):
		start, end, cost = map(int, sys.stdin.readline().rsplit())
		edges.append((cost, start, end))

	print(solution())