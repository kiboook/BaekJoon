import sys
from collections import deque


def BFS(arr, visit, l, n, m):
    # 4. 동, 서, 남, 북, 상, 하 이동 가능
    dirs = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]
    # 5. 시작 위치 탐색
    for k in range(l):
        for i in range(n):
            for j in range(m):
                if arr[k][i][j] == 'S':
                    # 6. 층, 행, 열, 분 저장
                    queue = deque([[k, i, j, 0]])
                    visit[k][i][j] = True
                    break

    while queue:
        now_l, now_n, now_m, minutes = queue.popleft()
        if arr[now_l][now_n][now_m] == 'E':
            return minutes

        # 7. 동, 서, 남, 북, 상, 하 탐색
        for value in dirs:
            visit_l, visit_n, visit_m = now_l + value[0], now_n + value[1], now_m + value[2]
            if 0 <= visit_l < l and 0 <= visit_n < n and 0 <= visit_m < m:
                if not visit[visit_l][visit_n][visit_m] and arr[visit_l][visit_n][visit_m] != '#':
                    queue.append([visit_l, visit_n, visit_m, minutes + 1])
                visit[visit_l][visit_n][visit_m] = True


def solution(l, n, m):
    # 1. 건물 정보 입력 받기
    arr = []
    for _ in range(l):
        tmp = [list(sys.stdin.readline()) for _ in range(n + 1)]
        tmp.pop()
        arr.append(tmp)

    # 2. 방문 여부 배열 생성
    visit = []
    for _ in range(l):
        tmp = [[False for _ in range(m)] for _ in range(n)]
        visit.append(tmp)

    # 3. 건물 탐색
    result = BFS(arr, visit, l, n, m)
    if result:
        print(f"Escaped in {result} minute(s).")
    else:
        print("Trapped!")


if __name__ == "__main__":
    while True:
        L, N, M = map(int, sys.stdin.readline().rsplit())
        if L + N + M == 0:
            break

        solution(L, N, M)


# 3 4 5
# S....
# .###.
# .##..
# ###.#
#
# #####
# #####
# ##.##
# ##...
#
# #####
# #####
# #.###
# ####E