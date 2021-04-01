import math
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

    edges = []
    for i in range(N):
        for j in range(i, N):
            if i != j:
                dist_x = (nodes[i][0] - nodes[j][0]) ** 2
                dist_y = (nodes[i][1] - nodes[j][1]) ** 2
                dist = round(math.sqrt(dist_x + dist_y), 2)
                edges.append([dist, i, j])
                edges.append([dist, j, i])
    edges.sort()

    for edge in edges:
        dist, start, end = edge
        if find_parent(start, parent) != find_parent(end, parent):
            union_parent(start, end, parent)
            answer += dist

    return answer


if __name__ == "__main__":
    N = int(input())
    nodes = [list(map(float, sys.stdin.readline().rsplit())) for _ in range(N)]

    print(solution())