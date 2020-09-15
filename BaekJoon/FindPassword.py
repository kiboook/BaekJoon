import sys

N, M = map(int, sys.stdin.readline().rsplit())
info = dict()

for _ in range(N):
	URL, password = sys.stdin.readline().rsplit()
	info[URL] = password

for _ in range(M):
	find = sys.stdin.readline().rsplit()[0]
	print(info[find])