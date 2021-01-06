import sys


def bellman():
	res = "NO"

	for _ in range(node_cnt):
		for node in graph:
			for visit in graph[node]:
				visit_node, road_weigth = visit
				if node_weight[visit_node] > node_weight[node] + road_weigth:
					node_weight[visit_node] = node_weight[node] + road_weigth

	for node in graph:
		for visit in graph[node]:
			visit_node, road_weigth = visit
			if node_weight[visit_node] > node_weight[node] + road_weigth:
				res = "YES"

	return res


INF = 100000000

if __name__ == '__main__':
	testcase = int(input())

	for _ in range(testcase):
		node_cnt, road_cnt, hole_cnt = map(int, input().split())
		graph = {i: [] for i in range(node_cnt)}
		node_weight = {i: INF for i in range(node_cnt)}
		node_weight[0] = 0

		for _ in range(road_cnt):
			start, end, weight = map(int, sys.stdin.readline().rsplit())
			graph[start - 1].append([end - 1, weight])
			graph[end - 1].append([start - 1, weight])

		for _ in range(hole_cnt):
			start, end, weight = map(int, sys.stdin.readline().rsplit())
			graph[start - 1].append([end - 1, weight * -1])

		print(bellman())