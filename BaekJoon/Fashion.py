import sys

test = int(input())
for _ in range(test):
	cloth_num = int(input())
	cloth = dict()

	for _ in range(cloth_num):
		item, cloth_type = sys.stdin.readline().rsplit()
		try:
			cloth[cloth_type] += 1
		except KeyError:
			cloth[cloth_type] = 1

	answer = 1
	for val in cloth.values():
		answer *= val + 1

	print(answer - 1)