import sys


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])

    return parent[node]


def solution(v, e):
    parent = [i for i in range(v)]
    edges = []
    total_money = 0
    # 1. MST를 만들기 위해 크루스칼 알고리즘을 사용한다.
    for _ in range(e):
        start, end, money = map(int, sys.stdin.readline().rsplit())
        total_money += money
        edges.append([money, start, end])
    edges.sort()

    # 2. 절약 금액은 총 금액에서 MST를 이루는 금액을 빼면 된다.
    # 3. Union-Find를 통해 사이클을 판별한다.
    min_money = 0
    for edge in edges:
        money, start, end = edge
        if find_parent(parent, start) != find_parent(parent, end):
            min_money += money
            union_parent(parent, start, end)

    return total_money - min_money


if __name__ == "__main__":
    while True:
        v, e = map(int, input().split())
        if v == 0 and e == 0:
            break
        else:
            print(solution(v, e))