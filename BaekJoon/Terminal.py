import sys


n = int(input())
answer = ''
arr = [sys.stdin.readline().rsplit()[0] for _ in range(n)]

for i in range(len(arr[0])):
	check = arr[0][i]
	for val in arr:
		if val[i] != check:
			answer += '?'
			break
	else:
		answer += check

print(answer)
