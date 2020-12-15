my_str = input()
answer = ""
stack = []

for val in my_str:
	if 'A' <= val <= 'Z':
		answer += val
	elif val == '(':
		stack.append(val)
	elif val == ')':
		while stack and stack[-1] != '(':
			answer += stack.pop()
		stack.pop()
	elif val == '*' or val == '/':
		while stack and (stack[-1] == '*' or stack[-1] == '/'):
			answer += stack.pop()
		stack.append(val)
	elif val == '+' or val == '-':
		while stack and stack[-1] != '(':
			answer += stack.pop()
		stack.append(val)

while stack:
	answer += stack.pop()

print(answer)
# A+B*C*D-E/F*G+H