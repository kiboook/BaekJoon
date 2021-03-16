import heapq


def solution(graph):
    for _ in range(N):
        start, end, dist = map(int, input().split())
        # 지름길인데 거리가 더 먼 경우, 출발점이나 도착점이 D 보다 큰 경우 필요 없음.
        if end - start < dist or start > D or end > D:
            continue
        else:
            graph[start].append([end, dist])

    for i in range(D):
        graph[i].append([i + 1, 1])

    distance = [float('inf')] * (D + 1)
    queue = []
    heapq.heappush(queue, [0, 0])
    while queue:
        now, dist = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, [i[0], cost])

    return distance[D]


if __name__ == "__main__":
    N, D = map(int, input().split())
    graph = {i: [] for i in range(D + 1)}

    print(solution(graph))