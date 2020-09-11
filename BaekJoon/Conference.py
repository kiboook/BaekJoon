from typing import List
import sys


def solution(conference: List) -> int:
	answer = 0
	end = 0

	for cur in conference:
		if cur[0] >= end:
			answer += 1
			end = cur[1]

	return answer


num = int(input())
_list = []

for _ in range(num):
	_list.append(list(map(int, sys.stdin.readline().rsplit())))

_list = sorted(_list, key=lambda a: (a[0], a[1]))
print(solution(_list))


# 5
# 4 10
# 4 4
# 1 2
# 3 4
# 2 3