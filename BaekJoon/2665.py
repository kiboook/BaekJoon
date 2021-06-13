from collections import deque


def BFS(n):
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input())))
    visit = [[False for _ in range(n)] for _ in range(n)]
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    queue = deque([[0, 0, 0]])
    visit[0][0] = True
    while queue:
        now_i, now_j, dark_room = queue.popleft()
        if now_i == n - 1 and now_j == n - 1:
            return dark_room

        for val in dirs:
            visit_i, visit_j = now_i + val[0], now_j + val[1]
            if 0 <= visit_i < n and 0 <= visit_j < n and not visit[visit_i][visit_j]:
                # 1. 검은 방인 경우 지나온 검은방 개수를 늘린 뒤 append
                if arr[visit_i][visit_j] == 0:
                    queue.append([visit_i, visit_j, dark_room + 1])
                # 2. 흰 방인 경우 먼저 방문하기 위해 appendleft
                else:
                    queue.appendleft([visit_i, visit_j, dark_room])
                visit[visit_i][visit_j] = True


def solution():
    n = int(input())

    return BFS(n)


if __name__ == "__main__":
    print(solution())