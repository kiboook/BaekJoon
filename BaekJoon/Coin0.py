def make_min_coin(coin, k):
	coin_cnt = 0

	for val in reversed(coin):
		coin_cnt += k // val
		k %= val

		if k == 0:
			break
	print(coin_cnt)


in_n, in_k = map(int, input().rsplit())
in_coin = []

for _ in range(in_n):
	in_coin.append(int(input()))

make_min_coin(in_coin, in_k)