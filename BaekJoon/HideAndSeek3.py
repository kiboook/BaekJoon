from collections import deque


def findMinTime(start, end):
	queue = deque([[start, 0]])
	visit = {start: 1}

	while queue:
		curNode, curSec = queue.popleft()

		if curNode == end:
			return curSec

		if curNode * 2 <= 1000000 and curNode * 2 not in visit:
			visit[curNode * 2] = 1
			queue.append([curNode * 2, curSec])

		if curNode - 1 >= 0 and curNode - 1 not in visit:
			visit[curNode - 1] = 1
			queue.append([curNode - 1, curSec + 1])

		if curNode + 1 <= 100000 and curNode + 1 not in visit:
			visit[curNode + 1] = 1
			queue.append([curNode + 1, curSec + 1])


n, k = map(int, input().split())
print(findMinTime(n, k))