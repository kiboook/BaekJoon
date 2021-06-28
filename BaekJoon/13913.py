import sys
from collections import deque


def solution():
    visit = [False] * 100_001
    path = [0] * 100_101
    queue = deque([[N, 0]])

    while queue:
        now, minutes = queue.popleft()
        # 1. 동생이 있는 곳에 도착했다면 지금까지 이동한 경로를 저장
        if now == K:
            route = []
            idx = K
            # 2. 도착지점부터 시작지점까지 거슬러 올라간다
            while idx != N:
                route.append(idx)
                idx = path[idx]
            route.append(N)
            route.reverse()
            print(minutes)
            print(*route)
            return

        # 3. 앞, 뒤, 순간이동으로 이동
        back, front, teleport = now - 1, now + 1, now * 2
        for move in (back, front, teleport):
            if 0 <= move <= 100_000 and not visit[move]:
                queue.append([move, minutes + 1])
                visit[move] = True
                path[move] = now


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())

    solution()