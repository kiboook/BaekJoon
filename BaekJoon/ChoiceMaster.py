def solution():

	for k in range(n):
		for i in range(n):
			for j in range(n):
				graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
				if i == j:
					graph[i][j] = 0

	score_list = [max(row) for row in graph]
	min_score = min(score_list)
	norminate = list()

	for i in range(len(score_list)):
		if score_list[i] == min_score:
			norminate.append(i + 1)

	print(min_score, len(norminate))
	print(*norminate)

	return


if __name__ == '__main__':
	n = int(input())
	graph = [[1_000_000] * n for _ in range(n)]

	while True:
		start, end = map(int, input().rsplit())
		if start == -1 and end == -1:
			break

		graph[start - 1][end - 1] = 1
		graph[end - 1][start - 1] = 1

	solution()