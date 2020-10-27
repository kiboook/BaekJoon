import sys
from collections import deque


def BFS(parent_arr, graph, know_truth, start):
	visit = []
	queue = deque([start])
	result = 0

	if start in parent_arr:
		result = 1

	while queue:
		cur_node = queue.popleft()
		if cur_node in know_truth:
			return 0

		visit.append(cur_node)

		for val in graph[cur_node]:
			if val not in visit:
				queue.append(val)
				visit.append(val)

	return result


def find_max_lie(party_arr, parent_arr, graph, know_truth):
	answer = 0

	for party in party_arr:
		answer += BFS(parent_arr, graph, know_truth, party[0])

	return answer


people_cnt, party_cnt = map(int, input().split())
know_cnt = list(map(int, input().split()))
party_arr = []
for _ in range(party_cnt):
	party = list(map(int, sys.stdin.readline().rsplit()))[1:]
	if len(party) == 0:
		continue
	else:
		party_arr.append(party)
if know_cnt[0] != 0:
	know_truth = [val for val in know_cnt[1:]]
else:
	know_truth = []

graph = {i + 1: [] for i in range(people_cnt)}
parent_arr = []

for party in party_arr:
	parent = party[0]
	parent_arr.append(party[0])
	for child in party[1:]:
		graph[parent].append(child)
		graph[child].append(parent)

print(find_max_lie(party_arr, parent_arr, graph, know_truth))

# 10 7
# 1 2
# 3 4 5 6
# 2 1 3
# 4 6 7 8 9
# 4 1 3 5 7
# 6 3 4 7 8 9 10
# 1 10
# 2 2 6

# 6 5
# 1 6
# 2 4 5
# 2 1 2
# 2 2 3
# 2 3 4
# 2 5 6

# 11 5
# 2 6 10
# 3 1 2 3
# 2 4 5
# 3 8 9 10
# 3 6 7 9
# 1 11

# 5 5
# 1 3
# 1 1
# 2 1 2
# 2 1 3
# 2 1 4
# 2 1 5

# 6 5
# 1 6
# 2 4 5
# 2 1 2
# 2 2 3
# 2 3 4
# 2 5 6

# 6 5
# 1 6
# 2 1 2
# 2 2 3
# 2 3 4
# 2 4 5
# 2 5 6

# 10 5
# 2 3 4
# 0
# 0
# 0
# 0
# 0