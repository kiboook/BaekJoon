import sys
from collections import deque


def solution():
    visit = dict()
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    horse_dirs = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, -1], [2, 1], [-1, -2], [1, -2]]
    queue = deque([(0, 0, 0, 0)])
    visit[(0, 0, 0)] = True

    while queue:
        now_i, now_j, now_dist, now_horse_cnt = queue.popleft()
        if now_i == N - 1 and now_j == M - 1:
            return now_dist

        for value in horse_dirs:
            visit_i, visit_j = now_i + value[0], now_j + value[1]
            if 0 <= visit_i < N and 0 <= visit_j < M and (visit_i, visit_j, now_horse_cnt + 1) not in visit:
                if field[visit_i][visit_j] != 1:
                    if now_horse_cnt < K:
                        visit[(visit_i, visit_j, now_horse_cnt + 1)] = True
                        queue.append((visit_i, visit_j, now_dist + 1, now_horse_cnt + 1))

        for value in dirs:
            visit_i, visit_j = now_i + value[0], now_j + value[1]
            if 0 <= visit_i < N and 0 <= visit_j < M and (visit_i, visit_j, now_horse_cnt) not in visit:
                if field[visit_i][visit_j] != 1:
                    visit[(visit_i, visit_j, now_horse_cnt)] = True
                    queue.append((visit_i, visit_j, now_dist + 1, now_horse_cnt))

    return -1


if __name__ == "__main__":
    K = int(input())
    M, N = map(int, input().split())
    field = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)]

    print(solution())