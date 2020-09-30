n = int(input())
time = sorted(list(map(int, input().split())))

tmp, answer = 0, 0
for val in time:
	tmp += val
	answer += tmp

print(answer)