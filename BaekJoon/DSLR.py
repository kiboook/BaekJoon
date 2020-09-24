import sys
from collections import deque


def find_min_route(a, b):

	visit = dict()
	start, end = a, b
	queue = deque([[start, '']])
	visit[start] = 1

	while queue:
		cur_node, cur_cal = queue.popleft()
		visit[cur_node] = 1
		D_i, S_i, L_i, R_i = D(cur_node), S(cur_node), L(cur_node), R(cur_node)

		if D_i not in visit:
			if D_i == end:
				return cur_cal + 'D'
			visit[D_i] = 1
			queue.append([D_i, cur_cal + 'D'])

		if S_i not in visit:
			if S_i == end:
				return cur_cal + 'S'
			visit[S_i] = 1
			queue.append([S_i, cur_cal + 'S'])

		if L_i not in visit:
			if L_i == end:
				return cur_cal + 'L'
			visit[L_i] = 1
			queue.append([L_i, cur_cal + 'L'])

		if R_i not in visit:
			if R_i == end:
				return cur_cal + 'R'
			visit[R_i] = 1
			queue.append([R_i, cur_cal + 'R'])


def D(a):
	return a * 2 % 10000


def S(a):
	return a - 1 if a != 0 else 9999


def L(a):
	return a % 1000 * 10 + a // 1000


def R(a):
	return a % 10 * 1000 + a // 10


for _ in range(int(input())):
	my_a, my_b = map(int, sys.stdin.readline().rsplit())
	print(find_min_route(my_a, my_b))
