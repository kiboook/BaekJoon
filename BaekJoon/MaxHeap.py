import heapq
import sys

N = int(input())
heap = []

for _ in range(N):
	data = int(sys.stdin.readline().rsplit()[0])

	if data == 0:
		if heap:
			print(heapq.heappop(heap) * -1)
		else:
			print(0)

	else:
		heapq.heappush(heap, data * -1)