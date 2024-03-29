import sys
from collections import deque


def solution():
    visit = [False for _ in range(101)]
    ladders, snakes = dict(), dict()
    ladders_cnt, snakes_cnt = map(int, input().split())

    for _ in range(ladders_cnt):
        start, end = list(map(int, sys.stdin.readline().rsplit()))
        ladders[start] = end
    for _ in range(snakes_cnt):
        start, end = list(map(int, sys.stdin.readline().rsplit()))
        snakes[start] = end

    # 1. BFS를 통해 탐색한다.
    queue = deque([[1, 0]])
    while queue:
        now, dice = queue.popleft()
        if now == 100:
            return dice

        for move in range(1, 7):
            # 2. 주사위 칸 만큼 이동한다.
            visit_node = now + move
            if 0 < visit_node <= 100 and not visit[visit_node]:
                # 3. 도착한 곳에 사다리가 있다면 사다리 끝으로 이동한다.
                if visit_node in ladders:
                    visit_node = ladders[visit_node]
                # 4. 도착한 곳에 뱀이 있다면 뱀 끝으로 이동한다.
                if visit_node in snakes:
                    visit_node = snakes[visit_node]

                queue.append([visit_node, dice + 1])
                visit[visit_node] = True


if __name__ == "__main__":
    print(solution())