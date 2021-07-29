# import sys
# from itertools import combinations
#
#
# def solution():
#     t = int(sys.stdin.readline())
#     a_len = int(sys.stdin.readline())
#     a = list(map(int, sys.stdin.readline().rsplit()))
#     b_len = int(sys.stdin.readline())
#     b = list(map(int, sys.stdin.readline().rsplit()))
#
#     a_prefix_sum = [0]
#     for i in range(a_len):
#         a_prefix_sum.append(a_prefix_sum[i] + a[i])
#
#     b_prefix_sum = [0]
#     for i in range(b_len):
#         b_prefix_sum.append(b_prefix_sum[i] + b[i])
#
#     a_sub = []
#     for idx in combinations([i for i in range(len(a_prefix_sum))], 2):
#         if a_prefix_sum[idx[1]] - a_prefix_sum[idx[0]] < t:
#             a_sub.append(a_prefix_sum[idx[1]] - a_prefix_sum[idx[0]])
#
#     b_sub = []
#     for idx in combinations([i for i in range(len(b_prefix_sum))], 2):
#         if b_prefix_sum[idx[1]] - b_prefix_sum[idx[0]] < t:
#             b_sub.append(b_prefix_sum[idx[1]] - b_prefix_sum[idx[0]])
#
#     answer = 0
#     for a_val in a_sub:
#         for b_val in b_sub:
#             if a_val + b_val == t:
#                 answer += 1
#
#     return answer
#
#
# if __name__ == "__main__":
#     print(solution())

import sys
from collections import defaultdict


def solution():
    T = int(sys.stdin.readline())
    a_len = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().rsplit()))
    b_len = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().rsplit()))

    # 1. a의 연속합을 저장한다.
    a_sum = dict()
    for i in range(a_len):
        for j in range(i, a_len):
            try:
                a_sum[sum(a[i:j + 1])] += 1
            except KeyError:
                a_sum[sum(a[i:j + 1])] = 1

    # 2. b의 연속합을 저장한다.
    b_sum = dict()
    for i in range(b_len):
        for j in range(i, b_len):
            try:
                b_sum[sum(b[i:j + 1])] += 1
            except KeyError:
                b_sum[sum(b[i:j + 1])] = 1

    # 3. 경우의 수를 구하는 것이기 때문에 곱셈으로 계산한다.
    answer = 0
    for key in a_sum:
        try:
            answer += b_sum[T - key] * a_sum[key]
        except KeyError:
            continue

    return answer


if __name__ == "__main__":
    print(solution())