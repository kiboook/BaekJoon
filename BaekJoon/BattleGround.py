import sys


def solution():
	for k in range(node_cnt):
		for i in range(node_cnt):
			for j in range(node_cnt):
				graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
				if i == j:
					graph[i][j] = 0

	res = 0
	for row in range(node_cnt):
		item_sum = 0
		for col in range(node_cnt):
			if graph[row][col] <= max_dist:
				item_sum += node_item[col]

		res = max(res, item_sum)
	return res


if __name__ == '__main__':
	node_cnt, max_dist, road_cnt = map(int, input().split())
	node_item = list(map(int, input().split()))
	graph = [[1_000_000] * node_cnt for _ in range(node_cnt)]

	for _ in range(road_cnt):
		start, end, dist = map(int, sys.stdin.readline().rsplit())
		graph[start - 1][end - 1] = min(graph[start - 1][end - 1], dist)
		graph[end - 1][start - 1] = min(graph[end - 1][start - 1], dist)

	print(solution())

