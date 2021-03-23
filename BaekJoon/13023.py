import sys


def DFS(parent, length, visit):
    visit.append(parent)

    if length == 5:
        print(1)
        exit(0)

    for node in graph[parent]:
        if node not in visit:
            DFS(node, length + 1, visit)
            visit.pop()


def solution():
    for i in range(N):
        DFS(i, 1, [])

    return 0


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = {i: [] for i in range(N)}

    for _ in range(M):
        start, end = map(int, sys.stdin.readline().rsplit())
        graph[start].append(end)
        graph[end].append(start)

    print(solution())