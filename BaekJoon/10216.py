import sys


def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])

    return parent[node]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution():
    answer = node_cnt
    parent = [i for i in range(node_cnt)]

    for i in range(node_cnt):
        for j in range(i + 1, node_cnt):
            x_dif = x_pos[i] - x_pos[j]
            y_dif = y_pos[i] - y_pos[j]
            dist = radius[i] + radius[j]

            if (x_dif ** 2) + (y_dif ** 2) <= dist ** 2:
                if find_parent(parent, i) != find_parent(parent, j):
                    union_parent(parent, i, j)
                    answer -= 1

    return answer


if __name__ == "__main__":
    testcase = int(input())

    for _ in range(testcase):
        node_cnt = int(input())
        x_pos, y_pos, radius = [], [], []
        for _ in range(node_cnt):
            x, y, r = map(int, sys.stdin.readline().rsplit())
            x_pos.append(x)
            y_pos.append(y)
            radius.append(r)

        print(solution())