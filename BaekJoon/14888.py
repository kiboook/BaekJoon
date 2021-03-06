from itertools import permutations


def calc_formula(nums, opers):
	nums = list(reversed(nums))
	opers = list(reversed(opers))

	while opers:
		a, oper, b = nums.pop(), opers.pop(), nums.pop()
		if int(a) < 0 and oper == '//':
			a = str(-int(a))
			formular = a + oper + b
			nums.append(str(-eval(formular)))
			continue

		formular = a + oper + b
		nums.append(str(eval(formular)))

	return int(nums[0])


def solution(n, nums, oper_cnt):
	answer_max = -float('inf')
	answer_min = float('inf')
	opers = []
	for oper, cnt in zip(['+', '-', '*', '//'], oper_cnt):
		opers.extend([oper] * cnt)

	for permutation in set(permutations(opers, n - 1)):
		num = calc_formula(nums, permutation)
		if num > answer_max:
			answer_max = num
		if num < answer_min:
			answer_min = num

	print(answer_max)
	print(answer_min)


if __name__ == '__main__':
	n = int(input())
	nums = list(input().split())
	oper_cnt = list(map(int, input().split()))

	solution(n, nums, oper_cnt)