import sys
from collections import Counter
from copy import deepcopy


MIN_AREA = float('INF')


di = [0, -1, 0, 1, 0]
dj = [0, 0, 1, 0, -1]
cctv_head = [0,
		[[1], [2], [3], [4]],
		[[1, 3], [2, 4]],
		[[1, 2], [2, 3], [3, 4], [4, 1]],
		[[1, 2, 4], [1, 2, 3], [2, 3, 4], [1, 3, 4]],
		[[1, 2, 3, 4]]]


def detection(office, start):
	global MIN_AREA

	if start == len(cctv):
		non_area = Counter(sum(office, []))[0]
		if MIN_AREA > non_area:
			MIN_AREA = non_area
		return

	cctv_num = cctv[start][0]
	cctv_i, cctv_j = cctv[start][1][0], cctv[start][1][1]
	for head in cctv_head[cctv_num]:
		tmp_office = deepcopy(office)
		for detect in head:
			visit_i = cctv_i
			visit_j = cctv_j
			while 0 <= visit_i < n and 0 <= visit_j < m:
				if tmp_office[visit_i][visit_j] == 0:
					tmp_office[visit_i][visit_j] = 1
				elif tmp_office[visit_i][visit_j] == 6:
					break
				visit_i += di[detect]
				visit_j += dj[detect]
		detection(tmp_office, start + 1)


if __name__ == '__main__':
	n, m = map(int, input().split())
	office = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(n)]

	cctv = list()
	for i in range(n):
		for j in range(m):
			if 1 <= office[i][j] <= 5:
				cctv.append([office[i][j], [i, j]])

	detection(office, 0)
	print(MIN_AREA)