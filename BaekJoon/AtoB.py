from collections import deque


def solution(start, goal):
	cnt = 1
	queue = deque([[start, cnt]])

	while queue:
		curNode, curCnt = queue.popleft()

		if curNode == goal:
			print(curCnt)
			return

		leftChild = curNode * 2
		rightChild = curNode * 10 + 1

		if leftChild <= 10**9:
			queue.append([leftChild, curCnt + 1])

		if rightChild <= 10**9:
			queue.append([rightChild, curCnt + 1])

	else:
		print(-1)
		return


n, m = map(int, input().split())
solution(n, m)