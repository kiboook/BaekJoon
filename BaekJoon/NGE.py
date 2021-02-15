import sys


def solution():
	answer = []
	max_num = []

	for num in reversed(arr):
		while max_num and max_num[-1] <= num:
			max_num.pop()

		if max_num:
			answer.append(max_num[-1])
			max_num.append(num)

		if not max_num:
			answer.append(-1)
			max_num.append(num)

	return list(reversed(answer))


if __name__ == '__main__':
	n = int(input())
	arr = list(map(int, sys.stdin.readline().rsplit()))

	print(*solution())

# 9
# 9 5 7 10 3 8 2 5 7