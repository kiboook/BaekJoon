from collections import deque


def elevator():
	queue = deque([[start, 0]])
	visit = {start: 1}

	while queue:
		floor, btn = queue.popleft()
		if floor > max_floor:
			break

		if floor == end:
			return btn

		if floor + up not in visit and floor + up <= max_floor:
			visit[floor + up] = 1
			queue.append([floor + up, btn + 1])

		if floor - down not in visit and floor - down >= 1:
			visit[floor - down] = 1
			queue.append([floor - down, btn + 1])

	return "use the stairs"


if __name__ == '__main__':
	max_floor, start, end, up, down = map(int, input().split())
	print(elevator())