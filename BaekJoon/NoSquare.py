import math


min_num, max_num = map(int, input().split())
result = [1 for i in range(max_num - min_num + 1)]
squares = [i ** 2 for i in range(2, int(math.sqrt(max_num)) + 1)]

for square in squares:
	cur_idx = math.ceil(min_num / square) * square - min_num

	while cur_idx <= max_num - min_num:
		result[cur_idx] = 0
		cur_idx += square

print(sum(result))