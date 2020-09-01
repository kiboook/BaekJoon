def check_VPS(val):
	_stack = []
	output = ''

	for i in val:
		if i == '(':
			_stack.append(i)
		elif i == ')':
			try:
				_stack.pop()
			except IndexError:
				output = 'NO'
				return print(output)

	if _stack:
		output = 'NO'
	else:
		output = 'YES'

	return print(output)


n = int(input())
parenthesis = []

for i in range(n):
	parenthesis.append(input())

for val in parenthesis:
	check_VPS(val)



