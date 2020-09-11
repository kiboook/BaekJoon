import heapq
import sys

n = int(input())

heap = []
for i in range(n):
	order = int(sys.stdin.readline())
	print(order)

	if order == 0:
		if heap:
			print(heapq.heappop(heap))
		else:
			print(0)

	else:
		heapq.heappush(heap, order)

# 9
# 0
# 12345678
# 1
# 2
# 0
# 0
# 0
# 0
# 32