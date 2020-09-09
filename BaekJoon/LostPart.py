import re


fomula = input()
fomula = re.split('([^0-9])', fomula)
cal = []
idx = 0

while idx < len(fomula):

	if fomula[idx] == '+':
		num1 = int(cal.pop())
		num2 = int(fomula[idx + 1])
		cal.append(str(num1 + num2))
		idx += 2

	elif fomula[idx] == '-':
		cal.append(fomula[idx])
		idx += 1

	else:
		cal.append(str(int(fomula[idx])))
		idx += 1

print(eval(''.join(cal)))

