import sys
from collections import deque


def BFS(field, sword):
    sword_time = -1
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    queue = deque([(0, 0, 0)])
    field[0][0] = 1

    while queue:
        now_i, now_j, time = queue.popleft()
        if (now_i, now_j) == sword:
            sword_time = time
        for value in dirs:
            visit_i, visit_j = now_i + value[0], now_j + value[1]
            if 0 <= visit_i < N and 0 <= visit_j < M and field[visit_i][visit_j] < 1:
                field[visit_i][visit_j] = time + 1
                queue.append((visit_i, visit_j, time + 1))

    return sword_time


def solution(field):
    sword = ()
    for i in range(N):
        for j in range(M):
            if field[i][j] == 2:
                field[i][j] = 0
                sword = (i, j)

    sword_time = BFS(field, sword)
    direct = field[N - 1][M - 1]
    if sword_time >= 0:
        sword_time += (N - 1) - sword[0] + (M - 1) - sword[1]

    # 검과 공주 둘 다 갈 수 없는 경우
    if direct == 0 and sword_time == -1:
        return "Fail"

    # 검에만 갈 수 있는 경우
    if direct == 0 and sword_time != -1:
        if sword_time <= limit:
            return sword_time
        else:
            return "Fail"

    # 공주에게만 갈 수 있는 경우
    if direct and sword_time == -1:
        if direct <= limit:
            return direct
        else:
            return "Fail"

    # 검과 공주 둘 다 갈 수 있는 경우
    answer = min(direct, sword_time)
    if answer <= limit:
        return answer
    else:
        return "Fail"


if __name__ == "__main__":
    N, M, limit = map(int, input().split())
    field = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)]

    print(solution(field))

