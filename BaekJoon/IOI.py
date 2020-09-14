import sys
import re


def solution1(N, str_size, string):
	count = pattern = idx = 0

	while idx < str_size - 1:
		if string[idx - 1] == 'I' and string[idx] == 'O' and string[idx + 1] == 'I':
			pattern += 1
			if pattern == N:
				count += 1
				pattern -= 1
			idx += 1

		else:
			pattern = 0
		idx += 1

	return count


def solution2(part, sub_len):
	count = 0
	for val in part:
		if len(val) >= sub_len:
			count += (len(val) - sub_len) // 2 + 1

	return count


N = int(sys.stdin.readline().rsplit()[0])
str_size = int(sys.stdin.readline().rsplit()[0])
_string = sys.stdin.readline().rsplit()[0]

print(solution1(N, str_size, _string))

part = re.findall('I(?:OI)+', _string)
print(solution2(part, 1 + 2 * N))