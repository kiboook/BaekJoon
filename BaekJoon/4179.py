import sys
from collections import deque


def solution():
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    character, fires = None, list()
    for i in range(N):
        for j in range(M):
            if field[i][j] == 'J':
                character = ('J', i, j, 0)
            elif field[i][j] == 'F':
                fires.append(('F', i, j, 0))

    visit = dict()
    queue = deque([])
    for fire in fires:
        visit[fire] = True
        queue.append(fire)
    visit[character] = True
    queue.append(character)

    while queue:
        who, now_i, now_j, time = queue.popleft()

        if now_i == 0 or now_i == N - 1 or now_j == 0 or now_j == M - 1:
            if who == 'J':
                return time + 1

        for value in dirs:
            visit_i, visit_j = now_i + value[0], now_j + value[1]
            if 0 <= visit_i < N and 0 <= visit_j < M and (who, visit_i, visit_j, time) not in visit:
                if who == 'F' and field[visit_i][visit_j] == '.':
                    field[visit_i][visit_j] = 'F'
                    visit[('F', visit_i, visit_j, time)] = True
                    queue.append(('F', visit_i, visit_j, time))
                elif who == 'J' and field[visit_i][visit_j] == '.':
                    field[visit_i][visit_j] = 'J'
                    visit[('J', visit_i, visit_j, time + 1)] = True
                    queue.append(('J', visit_i, visit_j, time + 1))

    return "IMPOSSIBLE"


if __name__ == "__main__":
    N, M = map(int, input().split())
    field = [list(sys.stdin.readline()) for _ in range(N)]

    print(solution())