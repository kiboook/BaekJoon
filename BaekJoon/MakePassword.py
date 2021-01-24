from itertools import combinations


if __name__ == '__main__':
	l, c = map(int, input().rsplit())
	data = sorted(input().rsplit())

	vowel = {'a', 'e', 'i', 'o', 'u'}
	for val in list(combinations(data, l)):
		if set(val) & vowel and len(set(val) - vowel) >= 2:
			print(''.join(val))