import sys


def DFS(node, edges, visit):
    now_visit = {}
    now_visit_len = 0
    stack = [node]
    visit[node] = True

    while stack:
        now = stack.pop()
        now_visit[now] = now_visit_len
        now_visit_len += 1

        if not visit[edges[now]]:
            visit[edges[now]] = True
            stack.append(edges[now])

        if edges[now] in now_visit:
            return now_visit_len - now_visit[edges[now]]

    return 0


def solution():
    N = int(input())
    visit = {i + 1: False for i in range(N)}
    edges = [0] + list(map(int, sys.stdin.readline().rsplit()))

    cycle_nodes = 0
    for node in range(1, N + 1):
        if not visit[node]:
            cycle_nodes += DFS(node, edges, visit)

    return N - cycle_nodes


if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        print(solution())