import sys
from collections import deque


def cal_relationship():
	queue = deque([[start, 0]])
	visit = {start: 1}

	while queue:
		cur_node, cur_dist = queue.popleft()
		if cur_node == end:
			return cur_dist

		for visit_node in graph[cur_node]:
			if visit_node not in visit:
				visit[visit_node] = 1
				queue.append([visit_node, cur_dist + 1])

	return -1


if __name__ == '__main__':
	person = int(input())
	start, end = map(int, input().split())
	graph = {i + 1: [] for i in range(person)}

	for _ in range(int(input())):
		parent, child = map(int, sys.stdin.readline().rsplit())
		graph[parent].append(child)
		graph[child].append(parent)

	print(cal_relationship())