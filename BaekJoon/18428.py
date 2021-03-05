import sys
from itertools import combinations
from copy import deepcopy


def findUp(field, teacher, n):
	i, j = teacher[0] - 1, teacher[1]
	while 0 <= i:
		if field[i][j] == 'S':
			return True
		elif field[i][j] == 'O':
			return False
		i -= 1
	return False


def findDown(field, teacher, n):
	i, j = teacher[0] + 1, teacher[1]
	while i < n:
		if field[i][j] == 'S':
			return True
		elif field[i][j] == 'O':
			return False
		i += 1
	return False


def findRight(field, teacher, n):
	i, j = teacher[0], teacher[1] + 1
	while j < n:
		if field[i][j] == 'S':
			return True
		elif field[i][j] == 'O':
			return False
		j += 1
	return False


def findLeft(field, teacher, n):
	i, j = teacher[0], teacher[1] - 1
	while 0 <= j:
		if field[i][j] == 'S':
			return True
		elif field[i][j] == 'O':
			return False
		j -= 1
	return False


def isFindStudent(field, teachers, walls, n):
	for wall in walls:
		field[wall[0]][wall[1]] = 'O'

	for teacher in teachers:
		# 선생님이 학생을 찾은 경우
		if findUp(field, teacher, n) or findDown(field, teacher, n) \
				or findRight(field, teacher, n) or findLeft(field, teacher, n):
			return True

	return False


def solution(n, field):
	empties = []
	teachers = []
	for i in range(n):
		for j in range(n):
			if field[i][j] == 'X':
				empties.append([i, j])
			elif field[i][j] == 'T':
				teachers.append([i, j])

	for walls in combinations(empties, 3):
		if isFindStudent(deepcopy(field), teachers, walls, n):
			continue
		else:
			return "YES"

	return "NO"


if __name__ == '__main__':
	n = int(input())
	field = [sys.stdin.readline().rsplit() for _ in range(n)]

	print(solution(n, field))
