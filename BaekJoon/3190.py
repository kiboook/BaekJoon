import sys
from collections import deque


def move(field, snake):
	next_i, next_j, time, head = snake[-1]
	if head == 'U':
		next_i -= 1
	if head == 'R':
		next_j += 1
	if head == 'D':
		next_i += 1
	if head == 'L':
		next_j -= 1

	if 0 <= next_i < len(field) and 0 <= next_j < len(field) and field[next_i][next_j] <= 1:
		# 이동 한 곳에 사과가 없는 경우
		if field[next_i][next_j] != 1:
			tail = snake.popleft()
			field[tail[0]][tail[1]] = 0

		field[next_i][next_j] = 9
		snake.append([next_i, next_j, time + 1, head])
		return True
	else:
		return False


def solution(field, orders):
	# i, j, time, head
	snake = deque([[0, 0, 0, 'R']])
	field[0][0] = 9

	sec = 0
	while True:
		sec += 1
		if not move(field, snake):
			return sec

		if orders:
			if snake[-1][2] == orders[-1][0]:
				time, dire = orders.pop()
				if snake[-1][3] == 'U':
					if dire == 'D':
						snake[-1][3] = 'R'
					elif dire == 'L':
						snake[-1][3] = 'L'
				elif snake[-1][3] == 'R':
					if dire == 'D':
						snake[-1][3] = 'D'
					elif dire == 'L':
						snake[-1][3] = 'U'
				elif snake[-1][3] == 'D':
					if dire == 'D':
						snake[-1][3] = 'L'
					elif dire == 'L':
						snake[-1][3] = 'R'
				elif snake[-1][3] == 'L':
					if dire == 'D':
						snake[-1][3] = 'U'
					elif dire == 'L':
						snake[-1][3] = 'D'


if __name__ == '__main__':
	n = int(input())
	field = [[0 for _ in range(n)] for _ in range(n)]

	for _ in range(int(input())):
		i, j = map(int, sys.stdin.readline().rsplit())
		field[i - 1][j - 1] = 1

	orders = []
	for _ in range(int(input())):
		order = list(sys.stdin.readline().rsplit())
		order[0] = int(order[0])
		orders.append(order)
	orders.sort(reverse=True)

	print(solution(field, orders))