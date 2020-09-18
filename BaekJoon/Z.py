N, r, c = map(int, input().split())
count = 0

while True:
	width = 2 ** (N - 1)

	if width == 1:
		if [r, c] == [0, 1]:
			count += 1
		elif [r, c] == [1, 0]:
			count += 2
		elif [r, c] == [1, 1]:
			count += 3
		break

	if r < width <= c:  # 2사분면
		count += width ** 2
		c -= width
	elif c < width <= r:  # 3사분면
		count += width ** 2 * 2
		r -= width
	elif r >= width and c >= width:  #4사분면
		count += width ** 2 * 3
		r -= width
		c -= width

	N -= 1

print(count)