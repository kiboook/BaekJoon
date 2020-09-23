import sys

t = int(input())
arr = [1, 2, 4]
for i in range(3, 11):
	arr.append(arr[i - 3] + arr[i - 2] + arr[i - 1])

for _ in range(t):
	num = sys.stdin.readline().rsplit()[0]
	print(arr[int(num) - 1])