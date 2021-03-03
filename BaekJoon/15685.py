import sys
from itertools import combinations


def initHousesAndChickens(n, field):
	houses = []
	chickens = []

	for i in range(n):
		for j in range(n):
			if field[i][j] == 1:
				houses.append([i, j])
			elif field[i][j] == 2:
				chickens.append([i, j])

	return [houses, chickens]


def calcChickenDist(house, chicken):
	return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])


def solution(n, m, field):
	houses, chickens = initHousesAndChickens(n, field)

	answer = float('inf')
	for chickens in combinations(chickens, m):
		city_chicken_dist = 0
		for house in houses:
			chicken_dist = float("inf")
			for chicken in chickens:
				chicken_dist = min(chicken_dist, calcChickenDist(house, chicken))
			city_chicken_dist += chicken_dist
		answer = min(answer, city_chicken_dist)

	return answer


if __name__ == '__main__':
	n, m = map(int, input().split())
	field = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(n)]

	print(solution(n, m, field))