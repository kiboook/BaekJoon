# def find_num(a, start, end, num):  Recursive ver.
# 	mid = (start + end) // 2
#
# 	if a[mid] == num:
# 		return print(1)
#
# 	if start == end:
# 		if a[mid] == num:
# 			return print(1)
# 		else:
# 			return print(0)
#
# 	if a[mid] > num:
# 		find_num(a, start, mid, num)
# 	else:
# 		find_num(a, mid + 1, end, num)
#
#
# for num in b:
# 	find_num(a, 0, len(a) - 1, num)

N = input()
a = sorted(list(map(int, input().split())))

M = input()
b = list(map(int, input().split()))


def find_num(a, start, end, num):

	while start <= end:
		mid = (start + end) // 2

		if a[mid] == num:
			print(1)
			break
		elif a[mid] < num:
			start = mid + 1
		elif a[mid] > num:
			end = mid - 1
	else:
		print(0)


for num in b:
	find_num(a, 0, len(a) - 1, num)
