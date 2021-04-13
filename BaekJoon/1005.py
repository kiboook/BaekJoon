import sys
from collections import deque


def topology_sort(graph, indegree, N, arr, dp):
    result = []
    queue = deque([])

    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now] + arr[i])
            if indegree[i] == 0:
                queue.append(i)


def solution():
    N, M = map(int, input().split())
    time = map(int, sys.stdin.readline().rsplit())
    arr = [0] * (N + 1)
    dp = [0] * (N + 1)

    for idx, value in enumerate(time):
        arr[idx + 1] = value
        dp[idx + 1] = value

    graph = {i + 1: [] for i in range(N)}
    indegree = [0] * (N + 1)
    for _ in range(M):
        start, end = map(int, sys.stdin.readline().rsplit())
        indegree[end] += 1
        graph[start].append(end)
    building = int(input())

    topology_sort(graph, indegree, N, arr, dp)
    return dp[building]


if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        print(solution())