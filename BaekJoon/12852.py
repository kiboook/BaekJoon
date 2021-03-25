from collections import deque


def solution():
    result = []
    queue = deque([N])

    while queue:
        now = queue.popleft()
        if now == 1:
            start, end = 1, visit[1]

            while end:
                result.append(start)
                start = end
                end = visit[start]
            result.append(N)
            result.reverse()
            print(len(result) - 1)
            print(*result)

        if now % 3 == 0 and not visit[now // 3]:
            queue.append(now // 3)
            visit[now // 3] = now
        if now % 2 == 0 and not visit[now // 2]:
            queue.append(now // 2)
            visit[now // 2] = now
        if not visit[now - 1]:
            queue.append(now - 1)
            visit[now - 1] = now


if __name__ == "__main__":
    N = int(input())
    visit = [0] * (N + 1)
    solution()