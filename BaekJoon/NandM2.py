import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().rsplit())
data = [i for i in range(1, n + 1)]
output = list(combinations(data, m))

for i in output:
	for val in i:
		print(val, end=" ")
	print()