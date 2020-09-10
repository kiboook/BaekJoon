import sys
from collections import Counter


N, M = map(int, input().split())

name = []

for i in range(N + M):
	input_name = sys.stdin.readline().rsplit()
	name.append(input_name[0])

output = []
for val in Counter(name).items():
	if val[1] == 2:
		output.append(val[0])

print(len(output))
for name in sorted(output):
	print(name)
