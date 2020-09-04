import sys


N, M = map(int, sys.stdin.readline().rsplit())

poketmon = {sys.stdin.readline().rsplit()[0]: i + 1 for i in range(N)}
poketmon_reverse = {value: key for key, value in poketmon.items()}
question = [input() for _ in range(M)]

for val in question:
	try:
		poketmon_num = int(val)
	except ValueError:
		print(poketmon[val])  # 포켓몬 이름을 통해 숫자 출력
		continue

	print(poketmon_reverse[poketmon_num])

