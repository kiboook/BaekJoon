import heapq


def solution():
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    break_wall_cnt = [[float('inf') for _ in range(M)] for _ in range(N)]
    break_wall_cnt[0][0] = 0
    queue = []
    heapq.heappush(queue, (0, 0, 0))

    while queue:
        wall, now_i, now_j = heapq.heappop(queue)
        if break_wall_cnt[now_i][now_j] < wall:
            continue

        for value in dirs:
            cost, visit_i, visit_j = wall, now_i + value[0], now_j + value[1]
            if 0 <= visit_i < N and 0 <= visit_j < M:
                if field[visit_i][visit_j] == 1:
                    cost += 1

                if cost < break_wall_cnt[visit_i][visit_j]:
                    break_wall_cnt[visit_i][visit_j] = cost
                    heapq.heappush(queue, (cost, visit_i, visit_j))

    return break_wall_cnt[N - 1][M - 1]


if __name__ == "__main__":
    M, N = map(int, input().split())
    field = [list(map(int, input())) for _ in range(N)]
    print(solution())