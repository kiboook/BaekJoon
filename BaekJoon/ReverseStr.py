from collections import deque


def solution(str):
	nums = deque(map(int, str))
	work = [0, 0]

	before = nums.popleft()
	while nums:
		now = nums.popleft()
		if before == now:
			before = now
			continue
		else:
			work[before] += 1
			before = now
	work[now] += 1

	return min(work)


if __name__ == '__main__':
	str = input()
	print(solution(str))