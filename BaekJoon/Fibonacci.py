def make_fibo():
	fibo = dict()
	fibo[0], fibo[1] = [1, 0], [0, 1]

	for i in range(2, 41):
		fibo[i] = [fibo[i - 1][0] + fibo[i - 2][0], fibo[i - 1][1] + fibo[i - 2][1]]
	return fibo


n = int(input())
arr = []
for _ in range(n):
	arr.append(int(input()))

fibo = make_fibo()
for num in arr:
	print(fibo[num][0], fibo[num][1])