a_size = int(input())
a = [int(val) for val in input().split()]
sort_a = sorted(a)

p = []
for i in range(a_size):
	p.append(sort_a.index(a[i]))
	sort_a[p[i]] = 1001

for val in p:
	print(val, end=' ')