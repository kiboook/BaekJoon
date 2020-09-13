import sys
import re
from collections import deque


def do_func(arr, func):
	R_cnt = 0

	for val in func:
		if val == 'R':
			R_cnt += 1

		if val == 'D':
			if R_cnt % 2 == 0:
				try:
					arr.popleft()
				except IndexError:
					return 'error'

			elif R_cnt % 2 != 0:
				try:
					arr.pop()
				except IndexError:
					return 'error'

	if R_cnt % 2 != 0:
		arr.reverse()

	return '[' + ','.join([str(x) for x in arr]) + ']'


testcase = int(input())
for _ in range(testcase):
	func = sys.stdin.readline().rsplit()[0]
	arr_size = int(sys.stdin.readline().rsplit()[0])

	if arr_size:
		arr = deque(map(int, re.split('[,]', sys.stdin.readline().rsplit()[0][1:-1])))
	else:
		sys.stdin.readline().rsplit()
		arr = deque([])

	print(do_func(arr, func))


# 4
# RDD
# 4
# [1,2,3,4]
# DD
# 1
# [42]
# RRD
# 6
# [1,1,2,3,5,8]
# D
# 0
# []