import sys
from collections import deque
from copy import deepcopy


def BFS(arr, i, j, size):
	arr_tmp = deepcopy(arr)
	dist_arr = [[0] * N for _ in range(N)]
	queue = deque([[i, j, 0]])
	dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

	while queue:
		start_i, start_j, dist = queue.popleft()
		arr_tmp[start_i][start_j] = 1_000_000

		for cur in dirs:
			visit_i, visit_j = start_i + cur[0], start_j + cur[1]
			if 0 <= visit_i < N and 0 <= visit_j < N and arr_tmp[visit_i][visit_j] <= size:
				arr_tmp[visit_i][visit_j] = 1_000_000
				dist_arr[visit_i][visit_j] = dist + 1
				queue.append([visit_i, visit_j, dist + 1])
	dist_arr[i][j] = 0
	return dist_arr


def solution(arr):
	size_cnt = 0
	answer = 0
	size = 2
	start = []

	for i in range(N):
		for j in range(N):
			if arr[i][j] == 9:
				start = [i, j]
				arr[i][j] = 0
	dist = BFS(arr, start[0], start[1], size)

	while True:
		re_i, re_j, check = 0, 0, 0
		
		go_cnt, over_cnt = 0, 0
		for i in range(N):
			for j in range(N):
				if dist[i][j] != 0:
					go_cnt += 1
					if arr[i][j] == 0 or arr[i][j] >= size:
						over_cnt += 1
		if go_cnt == over_cnt:  # 갈 수 있는 모든 곳이 0 이거나 size 이상이라면 종료
			break

		tmp = 1_000_000
		for i in range(N):
			for j in range(N):
				if 1 <= arr[i][j] < size and 0 < dist[i][j] < tmp:
					tmp = dist[i][j]
					re_i, re_j = i, j

		size_cnt += 1
		arr[re_i][re_j] = 0
		answer += dist[re_i][re_j]

		if size_cnt == size:
			size_cnt = 0
			size += 1

		dist = BFS(arr, re_i, re_j, size)

	print(answer)


N = int(input())
my_arr = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)]
solution(my_arr)