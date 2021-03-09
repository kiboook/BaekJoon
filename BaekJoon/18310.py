def solution():
	return houses[(n - 1) // 2]


if __name__ == '__main__':
	n = int(input())
	houses = sorted(list(map(int, input().split())))

	print(solution())