def check_balance(_str):
	_stack = []
	output = 'yes'

	for i in _str:
		if i == '(' or i == '[':
			_stack.append(i)

		elif i == ')':
			if not _stack:
				output = 'no'
				break
			if _stack[-1] == '(':
				_stack.pop()
			else:
				output = 'no'
				break

		elif i == ']':
			if not _stack:
				output = 'no'
				break
			if _stack[-1] == '[':
				_stack.pop()
			else:
				output = 'no'
				break

	if _stack:
		output = 'no'

	return print(output)


input_str = []
while True:
	tmp = input()
	if tmp == '.':
		break
	else:
		input_str.append(tmp)

for val in input_str:
	check_balance(val)

