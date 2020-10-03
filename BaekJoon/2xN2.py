from math import factorial


def cal(n, r, k):

	return (factorial(n) // (factorial(n - r) * factorial(r))) * k


answer = 0
weight = int(input())
n = weight
r = 0
k = 1

while n >= r:
	answer += cal(n, r, k)
	n -= 1
	r += 1
	k *= 2

print(answer % 10007)