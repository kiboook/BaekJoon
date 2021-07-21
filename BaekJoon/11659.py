import sys


def solution():
    N, M = map(int, sys.stdin.readline().rsplit())
    arr = list(map(int, sys.stdin.readline().rsplit()))
    prefix_sum = [0]
    for i in range(1, N + 1):
        prefix_sum.append(prefix_sum[i - 1] + arr[i - 1])

    for _ in range(M):
        start, end = map(int, sys.stdin.readline().rsplit())
        print(prefix_sum[end] - prefix_sum[start - 1])


if __name__ == "__main__":
    solution()