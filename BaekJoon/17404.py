import sys
from copy import deepcopy


def painting(paint):
    arr = deepcopy(info)
    if paint == 0:
        arr[0][1] = arr[0][2] = float('inf')
    if paint == 1:
        arr[0][0] = arr[0][2] = float('inf')
    if paint == 2:
        arr[0][0] = arr[0][1] = float('inf')

    for i in range(1, N):
        for j in range(3):
            if j == 0:
                arr[i][j] += min(arr[i - 1][j + 1], arr[i - 1][j + 2])
            if j == 1:
                arr[i][j] += min(arr[i - 1][j - 1], arr[i - 1][j + 1])
            if j == 2:
                arr[i][j] += min(arr[i - 1][j - 2], arr[i - 1][j - 1])
    arr[N - 1][paint] = float('inf')

    return min(arr[N - 1])


def solution():
    answer = float('inf')
    for i in range(3):
        answer = min(answer, painting(i))

    return answer


if __name__ == "__main__":
    N = int(input())
    info = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)]

    print(solution())