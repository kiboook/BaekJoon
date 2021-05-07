import sys
from collections import deque


def BFS(arr):
    melt_cheeze = 0
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    visit = [[False for _ in range(M)] for _ in range(N)]
    queue = deque([[0, 0]])

    while queue:
        now_i, now_j = queue.popleft()
        for val in dirs:
            visit_i, visit_j = now_i + val[0], now_j + val[1]
            if 0 <= visit_i < N and 0 <= visit_j < M and not visit[visit_i][visit_j]:
                if arr[visit_i][visit_j] == 0:
                    queue.append([visit_i, visit_j])
                else:
                    arr[visit_i][visit_j] = 0
                    melt_cheeze += 1
                visit[visit_i][visit_j] = True

    return melt_cheeze


def solution(arr):
    before_melt_cheeze = 0
    now_melt_cheeze = 0
    hour = 0

    # 1. 녹일 치즈가 없을 때 까지 반복한다.
    while True:
        now_melt_cheeze = BFS(arr)
        # 2. 이번 시간에 녹인 치즈가 없다면 정답을 반환한다.
        if now_melt_cheeze == 0:
            print(hour)
            print(before_melt_cheeze)
            return
        # 3. 이번 시간에 녹인 치즈가 있다면 시간을 늘리고 이전 시간에 녹인 치즈 개수를 저장한다.
        hour += 1
        before_melt_cheeze = now_melt_cheeze


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)]

    solution(arr)