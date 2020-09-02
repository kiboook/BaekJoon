n = int(input())
stack = []
order = []

for i in range(n):
	order.append(input().split(' '))

for val in order:
	if val[0] == 'push':
		stack.append(int(val[1]))
	elif val[0] == 'pop':
		if stack:
			print(stack.pop())
		else:
			print(-1)
	elif val[0] == 'top':
		if stack:
			print(stack[-1])
		else:
			print(-1)
	elif val[0] == 'size':
		print(len(stack))
	elif val[0] == 'empty':
		if stack:
			print(0)
		else:
			print(1)
