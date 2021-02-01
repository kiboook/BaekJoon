import copy
from collections import Counter

#  상, 하, 좌, 우
dir_i = [-1, 1, 0, 0]
dir_j = [0, 0, -1, 1]
detection_dir = [0, [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[1, 2], [1, 3], [0, 2], [0, 3]],
	  [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], [[0, 1, 2, 3]]]

MIN = float("INF")


def solution(cctv_idx, office, cctv_list):
	global MIN

	if cctv_idx == len(cctv_list):
		detection_area = Counter(sum(office, []))[0]
		MIN = min(MIN, detection_area)
		return

	cctv_num, cctv_i, cctv_j = cctv_list[cctv_idx]
	for cctv_dir in detection_dir[cctv_num]:
		tmp_office = copy.deepcopy(office)
		for i in cctv_dir:
			visit_i = cctv_i + dir_i[i]
			visit_j = cctv_j + dir_j[i]
			while 0 <= visit_i < n and 0 <= visit_j < m:
				if tmp_office[visit_i][visit_j] == 6:
					break
				elif tmp_office[visit_i][visit_j] == 0:
					tmp_office[visit_i][visit_j] = 9
				visit_i += dir_i[i]
				visit_j += dir_j[i]
		solution(cctv_idx + 1, tmp_office, cctv_list)


if __name__ == "__main__":
	n, m = map(int, input().rsplit())
	office = [list(map(int, input().rsplit())) for _ in range(n)]
	cctv_list = []
	for i in range(n):
		for j in range(m):
			if office[i][j] not in [0, 6]:
				cctv_list.append([office[i][j], i, j])

	solution(0, office, cctv_list)
	print(MIN)