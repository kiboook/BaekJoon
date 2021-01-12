if __name__ == '__main__':

	data = input()
	bomb = input()
	stack = list()
	len_bomb = len(bomb)
	last_bomb = bomb[-1]

	for char in data:
		stack.append(char)

		if stack[-1] == last_bomb and bomb == ''.join(stack[-len_bomb:]):
			for j in range(len_bomb):
				stack.pop()

	if stack:
		print(''.join(stack))
	else:
		print('FRULA')