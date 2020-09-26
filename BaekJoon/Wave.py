arr = [1, 1, 1, 2, 2]

for i in range(5, 100):
	arr.append(arr[i - 5] + arr[i - 1])

for _ in range(int(input())):
	print(arr[int(input()) - 1])