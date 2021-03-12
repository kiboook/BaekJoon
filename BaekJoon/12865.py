import sys


def solution():
    items = [(0, 0)]
    for _ in range(N):
        weight, value = map(int, sys.stdin.readline().rsplit())
        items.append((weight, value))

    for item in range(1, N + 1):
        for total_weigth in range(K + 1):
            item_weight, item_value = items[item]
            if item_weight <= total_weigth:
                dp[item][total_weigth] = max(dp[item - 1][total_weigth],
                                             dp[item - 1][total_weigth - item_weight] + item_value)
            else:
                dp[item][total_weigth] = dp[item - 1][total_weigth]

    return dp[N][K]


if __name__ == "__main__":
    N, K = map(int, input().split())
    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    print(solution())