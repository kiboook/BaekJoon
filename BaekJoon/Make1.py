N = int(input())
answer = 0
num_dict = {
	1: 0,
	2: 1,
	3: 1
}

for i in range(4, N + 1):
	check = []
	if i % 3 == 0:
		check.append(num_dict[i // 3])

	if i % 2 == 0:
		check.append(num_dict[i // 2])

	check.append(num_dict[i - 1])

	num_dict[i] = 1 + min(check)

print(num_dict[N])