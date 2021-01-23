import sys


if __name__ == '__main__':
	n = int(input())
	standard = ''.join(sys.stdin.readline().rsplit())

	m = int(input())
	check_list = list()
	for _ in range(m):
		check_list.append(''.join(sys.stdin.readline().rsplit()))

	standard_list = dict()
	for i in range(len(standard)):
		standard_list[standard[i:] + standard[:i]] = 1

	reverse = list(reversed(standard))
	for i in range(n):
		if reverse[i] == '1':
			reverse[i] = '3'
		elif reverse[i] == '2':
			reverse[i] = '4'
		elif reverse[i] == '3':
			reverse[i] = '1'
		elif reverse[i] == '4':
			reverse[i] = '2'

	reverse_standard = ''.join(reverse)
	for i in range(len(reverse_standard)):
		standard_list[reverse_standard[i:] + reverse_standard[:i]] = 1

	answer = list()
	for check in check_list:
		if check in standard_list:
			answer.append(' '.join(check))

	print(len(answer))
	for val in answer:
		print(val)