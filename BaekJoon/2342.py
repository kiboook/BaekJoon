# def cal_score(cur, move):
#     if cur == move:
#         return 1
#     if cur == 0:
#         return 2
#     if abs(cur - move) == 2:
#         return 4
#     else:
#         return 3
#
#
# def solution(orders):
#     # 1. 같은 곳 밟기 = 1점
#     # 2. 중앙에서 다른곳 = 2점
#     # 3. 대각선으로 이동 = 3점
#     # 4. 반대 방향으로 이동 = 4점
#     answer = 0
#
#     left = right = 0
#     for order in orders:
#         if order == 0:
#             return answer
#         # 5. 왼발, 오른발이 가는 경우 점수가 더 낮은 발로 이동, 점수가 같다면 왼발로?
#         left_score = cal_score(left, order)
#         right_score = cal_score(right, order)
#
#         if left_score <= right_score:
#             left = order
#             answer += left_score
#         else:
#             right = order
#             answer += right_score
#
#
# if __name__ == "__main__":
#     orders = list(map(int, input().split()))
#     print(solution(orders))

import sys

sys.setrecursionlimit(10 ** 6)


def cal_score(cur, move):
    if cur == move:
        return 1
    if cur == 0:
        return 2
    if abs(cur - move) == 2:
        return 4
    else:
        return 3


def solve(n, l, r):
    global dp
    if arr[n] == 0:
        return 0

    if dp[n][l][r] != -1:
        return dp[n][l][r]

    dp[n][l][r] = min(solve(n + 1, arr[n], r) + cal_score(l, arr[n]), solve(n + 1, l, arr[n]) + cal_score(r, arr[n]))

    return dp[n][l][r]


arr = list(map(int, sys.stdin.readline().split()))
dp = [[[-1] * 5 for _ in range(5)] for _ in range(100000)]
print(solve(0, 0, 0))