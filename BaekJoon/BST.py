import sys


def postOrder(start, end):
	if start > end:
		return

	pivot = end + 1
	for i in range(start + 1, end + 1):
		if data[i] > data[start]:
			pivot = i
			break

	postOrder(start + 1, pivot - 1)
	postOrder(pivot, end)
	print(data[start])


sys.setrecursionlimit(10 ** 9)
data = []
while True:
	try:
		data.append(int(input()))
	except:
		break

postOrder(0, len(data) - 1)
