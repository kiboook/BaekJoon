import sys
from itertools import combinations


def solution(arr, N, M):
	home = []
	chicken = []

	for i in range(N):
		for j in range(N):
			if arr[i][j] == 1:
				home.append([i, j])
			elif arr[i][j] == 2:
				chicken.append([i, j])

	answer = 1_000_000
	for i in combinations(chicken, M):
		min_chicken = 0
		for j in home:
			tmp = 1_000_000
			for k in i:
				dist = abs(j[0] - k[0]) + abs(j[1] - k[1])
				if dist < tmp:
					tmp = dist
			min_chicken += tmp
		if min_chicken < answer:
			answer = min_chicken

	return answer


N, M = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)]
print(solution(arr, N, M))