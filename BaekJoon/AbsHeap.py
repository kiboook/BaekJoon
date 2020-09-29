import heapq
import sys

positive_heap = []
negative_heap = []
for _ in range(int(input())):
	data = int(sys.stdin.readline().rsplit()[0])

	if data > 0:
		heapq.heappush(positive_heap, data)
	elif data < 0:
		heapq.heappush(negative_heap, -data)
	else:
		if positive_heap and negative_heap:
			if positive_heap[0] < negative_heap[0]:
				print(heapq.heappop(positive_heap))
			else:
				print(-heapq.heappop(negative_heap))
		else:
			if positive_heap:
				print(heapq.heappop(positive_heap))
			elif negative_heap:
				print(-heapq.heappop(negative_heap))
			else:
				print(0)