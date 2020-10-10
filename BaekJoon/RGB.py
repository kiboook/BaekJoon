import sys


def solution(arr, N):
	for i in range(1, N):
		for j in range(3):
			if j == 0:
				arr[i][j] += min(arr[i - 1][j + 1], arr[i - 1][j + 2])
			elif j == 1:
				arr[i][j] += min(arr[i - 1][j - 1], arr[i - 1][j + 1])
			elif j == 2:
				arr[i][j] += min(arr[i - 1][j - 2], arr[i - 1][j - 1])

	print(min(arr[N - 1]))


N = int(input())
arr = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)]
solution(arr, N)