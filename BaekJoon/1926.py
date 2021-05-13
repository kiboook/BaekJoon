from collections import deque


def BFS(visit, start):
    visit[start[0]][start[1]] = True
    queue = deque([start])
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    draw_size = 1

    while queue:
        now_i, now_j = queue.popleft()
        # 3. 시계방향으로 탐색 시작.
        for val in dirs:
            visit_i = now_i + val[0]
            visit_j = now_j + val[1]
            # 4. 배열 안에 있으며 방문한 적이 없고 그림이라면 큐에 넣는다.
            if 0 <= visit_i < N and 0 <= visit_j < M and not visit[visit_i][visit_j]:
                if arr[visit_i][visit_j] == 1:
                    queue.append([visit_i, visit_j])
                    # 5. 방문 한 횟수가 그림 크기이기 때문에 크기를 더해준다.
                    draw_size += 1
                visit[visit_i][visit_j] = True

    return draw_size


def solution():
    draw_cnt = 0
    draw_size = 0

    # 1. 방문 여부를 관리할 배열 생성.
    visit = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            # 2. 방문 하지 않고 그림인 부분부터 탐색 시작.
            if not visit[i][j] and arr[i][j] == 1:
                draw_cnt += 1
                draw_size = max(draw_size, BFS(visit, [i, j]))

    print(draw_cnt)
    print(draw_size)


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    solution()