from collections import deque


def checkMinSec(start):
	queue = deque([[start, 0]])
	visit = {start: 1}
	sec = 1000000
	minRoute = 0

	while queue:
		curNode, curSec = queue.popleft()
		visit[curNode] = 1

		if curSec > sec:
			continue

		if curNode == k:
			minRoute += 1
			if curSec < sec:
				sec = curSec

		if curNode - 1 >= 0 and curNode - 1 not in visit:
			queue.append([curNode - 1, curSec + 1])

		if curNode + 1 <= 100000 and curNode + 1 not in visit:
			queue.append([curNode + 1, curSec + 1])

		if curNode * 2 <= 100000 and curNode * 2 not in visit:
			queue.append([curNode * 2, curSec + 1])

	return sec, minRoute


n, k = map(int, input().split())
minSec, routeCnt = checkMinSec(n)
print(minSec)
print(routeCnt)