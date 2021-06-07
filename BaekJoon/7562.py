from collections import deque


def BFS(n, start, end):
    # 1. n * n  배열 초기화
    arr = [[0 for _ in range(n)] for _ in range(n)]
    # 2. 방문여부 확인
    arr[start[0]][start[1]] = 1
    # 3. 나이트 이동 방향
    dirs = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]

    # 4. 이동횟수 추가 후 큐에 삽입
    start.append(0)
    queue = deque([start])

    # 5. BFS 수행
    while queue:
        now_i, now_j, move_cnt = queue.popleft()
        if now_i == end[0] and now_j == end[1]:
            return move_cnt

        for val in dirs:
            visit_i, visit_j = now_i + val[0], now_j + val[1]
            if 0 <= visit_i < n and 0 <= visit_j < n and arr[visit_i][visit_j] == 0:
                queue.append([visit_i, visit_j, move_cnt + 1])
                arr[visit_i][visit_j] = 1


def solution():
    n = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    return BFS(n, start, end)


if __name__ == "__main__":
    for _ in range(int(input())):
        print(solution())