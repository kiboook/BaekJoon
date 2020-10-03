def init_fac(fac):
	for i in range(3, 1001):
		fac.append(fac[i - 1] * i)


def cal(n, r):
	return fac[n] // (fac[n - r] * fac[r])


fac = [1, 1, 2]
init_fac(fac)

answer = 0
weight = int(input())
n = weight
r = 0

while n >= r:
	answer += cal(n, r)
	n -= 1
	r += 1

print(answer % 10007)