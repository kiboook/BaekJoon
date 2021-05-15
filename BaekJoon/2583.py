from collections import deque


def BFS(visit, start):
    visit[start[0]][start[1]] = True
    queue = deque([start])
    empty_size = 1
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    while queue:
        now_i, now_j = queue.popleft()

        for value in dirs:
            visit_i, visit_j = now_i + value[0], now_j + value[1]
            if 0 <= visit_i < N and 0 <= visit_j < M and not visit[visit_i][visit_j]:
                if arr[visit_i][visit_j] == 0:
                    queue.append([visit_i, visit_j])
                    empty_size += 1
                visit[visit_i][visit_j] = True

    return empty_size


def solution(arr):

    # 1. 주어진 사각형 그리기
    for square in squares:
        weight = square[2] - square[0]
        height = square[3] - square[1]

        # 2. 가로, 세로 길이를 구해 사각형 그리기
        for i in range(square[1], square[1] + height):
            for j in range(square[0], square[0] + weight):
                arr[i][j] = 1

    empty_cnt = 0
    empty_size = []
    visit = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            # 3. 빈 공간 발견 시 탐색 시작
            if arr[i][j] == 0 and not visit[i][j]:
                empty_size.append(BFS(visit, [i, j]))
                empty_cnt += 1

    print(empty_cnt)
    print(*sorted(empty_size))


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    squares = [list(map(int, input().split())) for _ in range(K)]
    arr = [[0 for _ in range(M)] for _ in range(N)]

    solution(arr)