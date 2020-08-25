from collections import deque


def make_arr(arr, num):
	stack = []
	answer = []

	while True:

		if stack:
			while stack and stack[-1] == arr[0]:
				stack.pop()
				arr.popleft()
				answer.append('-')

		# try:
		# 	stack.append(num.pop())
		# except IndexError:
		# 	if len(stack) > 0:
		# 		return print('NO')
		# 	else:
		# 		break
		# answer.append('+')

		if not num:
			if stack:
				return print('NO')
			else:
				break
		else:
			stack.append(num.pop())
			answer.append('+')

	for val in answer:
		print(val)


n = int(input())
num = [i for i in reversed(range(1, n + 1))]
arr = deque([int(input()) for i in range(n)])

make_arr(arr, num)