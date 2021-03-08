def solution():
	answer = 0
	start = field[1] - field[0]
	end = field[-1] - field[0]

	while start <= end:
		mid = (start + end) // 2

		antenna = field[0]
		antenna_cnt = 1
		for i in range(1, n):
			if field[i] >= (antenna + mid):
				antenna = field[i]
				antenna_cnt += 1

		if antenna_cnt >= c:
			start = mid + 1
			answer = mid
		else:
			end = mid - 1

	return answer


if __name__ == '__main__':
	n, c = map(int, input().split())
	field = [int(input()) for _ in range(n)]
	field.sort()

	print(solution())