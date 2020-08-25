def B_first(arr):
	change = 0
	idx = 0
	for i in range(8):
		for _ in range(8):
			if i % 2 == 0:
				if idx % 2 == 0 and arr[idx] == 'W':
					change += 1
				if idx % 2 != 0 and arr[idx] == 'B':
					change += 1
			else:
				if idx % 2 == 0 and arr[idx] == 'B':
					change += 1
				if idx % 2 != 0 and arr[idx] == 'W':
					change += 1
			idx += 1
	return change


def W_first(arr):
	change = 0
	idx = 0
	for i in range(8):
		for _ in range(8):
			if i % 2 == 0:
				if idx % 2 == 0 and arr[idx] == 'B':
					change += 1
				if idx % 2 != 0 and arr[idx] == 'W':
					change += 1
			else:
				if idx % 2 == 0 and arr[idx] == 'W':
					change += 1
				if idx % 2 != 0 and arr[idx] == 'B':
					change += 1
			idx += 1
	return change


answer = []
n, m = map(int, input().split())

chess = []
for i in range(n):
	tmp = input()
	chess.append(tmp)

for i in range(n - 7):
	for j in range(m - 7):
		cut_chess = []
		start_i = i
		start_j = j
		for k in range(8):
			tmp = chess[start_i][start_j:start_j + 8]
			start_i += 1
			cut_chess.append(tmp)

		_join = ''.join(cut_chess)
		answer.append(min(W_first(_join), B_first(_join)))

print(min(answer))

# 10 13
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# WWWWWWWWWWBWB
# WWWWWWWWWWBWB