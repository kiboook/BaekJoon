def cut_tree(tress, height):
	output = 0
	for val in trees:
		if val - height > 0:
			output += val - height

	return output


def find_max_height(trees, m):
	right = max(trees) - 1
	left = 0

	if m == 1:
		return right

	while True:
		mid = (left + right) // 2

		output = cut_tree(trees, mid)
		if mid == left:
			return left

		if output >= m:  # 이 높이는 요구하는 나무의 높이를 충족한다.
			left = mid
		else:  #  이 높이는 요구하는 나무의 높이를 충족하지 못 한다.
			right = mid


n, m = map(int, input().split())
trees = list(map(int, input().split()))
print(find_max_height(trees, m))
