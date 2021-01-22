def cal_clock_num(card):
	num = int(card)

	for idx in range(1, 4):
		tmp = int(card[idx:4] + card[:idx])
		if num > tmp:
			num = tmp

	return num


if __name__ == '__main__':
	data = ''.join(list(input().rsplit()))
	clock_num = cal_clock_num(data)

	cnt = 0
	for i in range(1111, 10000):
		i_card_clock_num = cal_clock_num(str(i))
		if i == i_card_clock_num:
			cnt += 1
			if i == clock_num:
				print(cnt)
				exit(0)