import sys


def solution():
	answer = [0]
	receive_tower = []

	for i in range(1, len(towers)):
		if towers[i - 1] > towers[i]:
			answer.append(i)
			receive_tower.append([towers[i - 1], i])
		else:
			while receive_tower:
				if receive_tower[-1][0] < towers[i]:
					receive_tower.pop()
				else:
					answer.append(receive_tower[-1][1])
					receive_tower.append([towers[i], i + 1])
					break
			if not receive_tower:
				answer.append(0)
				receive_tower.append([towers[i], i + 1])

	print(*answer)

	return


if __name__ == '__main__':
	n = int(input())
	towers = list(map(int, sys.stdin.readline().rsplit()))
	solution()