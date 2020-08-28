def make_lan(lan, m):
	output = 0
	for val in lan:
		output += val // m

	return output


def cut_lan(lan, n):
	left = 0
	right = min(lan)

	if make_lan(lan, right) == n:
		return right

	while True:
		mid = (left + right) // 2
		if left == mid:
			return mid

		if make_lan(lan, mid) < n:
			right = mid
		else:
			left = mid


k, n = map(int, input().split())

lan = []
for i in range(k):
	lan.append(int(input()))

print(cut_lan(lan, n))





