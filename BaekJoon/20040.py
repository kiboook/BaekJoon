import sys


def find_parent(node, parent):
    if parent[node] != node:
        parent[node] = find_parent(parent[node], parent)

    return parent[node]


def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution():
    answer = 0

    parent = [i for i in range(N)]
    for idx, edge in enumerate(edges):
        a, b = edge
        if find_parent(a, parent) != find_parent(b, parent):
            union_parent(a, b, parent)
        else:
            answer = idx + 1
            break

    return answer


if __name__ == "__main__":
    N, M = map(int, input().split())
    edges = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(M)]

    print(solution())
