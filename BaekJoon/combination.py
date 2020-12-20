import sys


fac = [1, 1, 2]
n, m = map(int, sys.stdin.readline().rsplit())

for i in range(3, n + 1):
	fac.append(fac[i - 1] * i)

print(fac[n] // (fac[m] * fac[n - m]))

# import sys
# from math import factorial
#
#
# n, m = map(int, sys.stdin.readline().rsplit())
# print(factorial(n) / (factorial(n) * factorial(n - m)))