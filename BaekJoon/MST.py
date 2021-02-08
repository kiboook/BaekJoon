import sys


def solution():
	global edge_info
	edge_info.sort(key=lambda x: x[2])
	answer = 0
	connection = {i: 0 for i in range(1, V + 1)}
	connection[1] = 1
	connection_len = 1

	while connection_len != V:
		for idx, edge in enumerate(edge_info):
			if connection[edge[0]] >= 1 and connection[edge[1]] >= 1:
				continue

			if connection[edge[0]] >= 1 or connection[edge[1]] >= 1:
				answer += edge[2]
				connection_len += 1
				connection[edge[0]] += 1
				connection[edge[1]] += 1
				edge_info.pop(idx)
				break

	return answer


if __name__ == "__main__":
	V, E = map(int, input().split())
	edge_info = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(E)]

	print(solution())