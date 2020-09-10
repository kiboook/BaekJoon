# -------------------------------------------- #

# import re
# from math import factorial
#
#
# num = int(input())
# fac = str(factorial(num))[::-1]
#
# zero = re.split('[1-9]', fac)[0]
# print(len(zero))
#
# num = int(input())
# fac = 1
#
# for i in range(1, num + 1):
# 	fac *= i
#
# print(fac)
# print(factorial(num))

# -------------------------------------------- #

# import re
# from math import factorial
#
#
# num = int(input())
# fac = 1
#
# for i in range(1, num + 1):
# 	fac *= i
#
# zero = re.split('[1-9]', str(fac))[0]
# print(len(zero))

# -------------------------------------------- #

num = int(input())
fac = 1

for i in range(1, num + 1):
	fac *= i

zero = 0
for i in str(fac)[::-1]:
	if i == '0':
		zero += 1
	else:
		break

print(zero)