import sys
from collections import deque


def route_cnt_BFS(start):
	visited = dict()
	queue = deque([[start, 0]])
	total_route = 0

	while queue:
		visited_ver, route = queue.popleft()
		visited[visited_ver] = 1
		total_route += route

		for connected_ver in friends[visited_ver]:
			if connected_ver not in visited:
				queue.append([connected_ver, route + 1])
				visited[connected_ver] = 1

	return total_route


N, M = map(int, sys.stdin.readline().rsplit())
friends = {i + 1: [] for i in range(N)}

for _ in range(M):
	start, end = map(int, sys.stdin.readline().rsplit())
	friends[start].append(end)
	friends[end].append(start)

answer = [0, 1000000]
for start in range(1, N + 1):
	kevin_num = route_cnt_BFS(start)
	if kevin_num < answer[1]:
		answer = [start, kevin_num]

print(answer[0])



