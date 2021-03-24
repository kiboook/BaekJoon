import sys
import heapq
from copy import deepcopy


def solution():
    distance = [[float('inf'), [start]] for _ in range(N + 1)]
    distance[start][0] = 0

    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now][0] < dist:
            continue

        for edge in graph[now]:
            visit, cost = edge
            if dist + cost < distance[visit][0]:
                tmp = deepcopy(distance[now][1])
                tmp.append(visit)
                distance[visit][1] = tmp
                distance[visit][0] = dist + cost
                heapq.heappush(queue, (dist + cost, visit))

    print(distance[end][0])
    print(len(distance[end][1]))
    print(*distance[end][1])


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    graph = {i + 1: [] for i in range(N)}

    for _ in range(M):
        start, end, cost = map(int, sys.stdin.readline().rsplit())
        graph[start].append((end, cost))

    start, end = map(int, sys.stdin.readline().rsplit())

    solution()