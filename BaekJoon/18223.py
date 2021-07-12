import sys
import heapq


def dijkstra(graph, start):
    distance = [float('inf') for _ in range(len(graph) + 1)]
    distance[start] = 0
    queue = []
    heapq.heappush(queue, [start, 0])

    while queue:
        now, cost = heapq.heappop(queue)
        if distance[now] < cost:
            continue

        for edge_info in graph[now]:
            node, dist = edge_info
            dist += cost
            if dist < distance[node]:
                distance[node] = dist
                heapq.heappush(queue, [node, dist])

    return distance


if __name__ == "__main__":
    V, E, P = map(int, input().split())
    # 1. 주어진 조건에 맞게 그래프를 초기화 한다.
    graph = {i + 1: [] for i in range(V)}
    for _ in range(E):
        start, end, cost = map(int, sys.stdin.readline().rsplit())
        graph[start].append([end, cost])
        graph[end].append([start, cost])

    # 2. 출발점에서 마산까지 바로 가는 최단거리를 구한다.
    distance = dijkstra(graph, 1)
    direct = distance[V]
    save = distance[P]

    # 3. 출발점에서 건우까지 바로 가는 최단거리를 구한다.
    distance = dijkstra(graph, P)
    save += distance[V]

    # 4. 출발점에서 건우를 거쳐 마산까지 가는 거리와 바로 마산까지 가는 거리가 같다면 구할 수 있다.
    if save == direct:
        print("SAVE HIM")
    else:
        print("GOOD BYE")