import sys


def solution(arr):
	sort_arr = sorted(list(set(arr)))
	store_index = dict()

	for idx, val in enumerate(sort_arr):
		store_index[val] = idx

	answer = []
	for num in arr:
		answer.append(store_index[num])

	for cur in answer:
		print(cur, end=' ')


N = int(input())
input_arr = list(map(int, sys.stdin.readline().rsplit()))
solution(input_arr)