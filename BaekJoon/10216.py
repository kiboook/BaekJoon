import sys
from collections import deque


def BFS(visit, start):
	queue = deque([nodes[start]])
	visit[start] = True

	while queue:
		x1, y1, r1 = queue.popleft()

		for idx, node in enumerate(nodes):
			if not visit[idx]:
				x2, y2, r2 = node
				dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
				if dist <= (r1 + r2) ** 2:
					visit[idx] = True
					queue.append(node)


def solution():
	visit = [False] * node_cnt
	BFS_cnt = 0

	for idx, node in enumerate(nodes):
		if not visit[idx]:
			BFS(visit, idx)
			BFS_cnt += 1

	return BFS_cnt


if __name__ == "__main__":
	testcase = int(input())

	for _ in range(testcase):
		node_cnt = int(input())
		nodes = []
		for _ in range(node_cnt):
			x, y, r = map(int, sys.stdin.readline().rsplit())
			nodes.append([x, y, r])

		print(solution())