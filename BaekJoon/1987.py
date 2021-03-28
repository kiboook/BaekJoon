import sys


def solution():
    global answer, cnt
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    stack = {(0, 0, field[0][0])}
    while stack:
        now_i, now_j, path = stack.pop()
        cnt += 1
        answer = max(answer, len(path))

        for value in dirs:
            visit_i, visit_j = now_i + value[0], now_j + value[1]
            if 0 <= visit_i < N and 0 <= visit_j < M and field[visit_i][visit_j] not in path:
                stack.add((visit_i, visit_j, path + field[visit_i][visit_j]))


if __name__ == "__main__":
    answer = -float('inf')
    cnt = 0
    N, M = map(int, input().split())
    field = [list(sys.stdin.readline()) for _ in range(N)]

    solution()
    print(answer)
    print(cnt)