import sys


def solution():
    a, b = 0, 0

    for i in range(N):
        a += coord_x[i] * coord_y[i + 1]
        b += coord_x[i + 1] * coord_y[i]

    return abs((a - b) / 2)


if __name__ == "__main__":
    N = int(input())
    coord_x = []
    coord_y = []

    for _ in range(N):
        coord = tuple(map(int, sys.stdin.readline().split()))
        coord_x.append(coord[0])
        coord_y.append(coord[1])

    coord_x.append(coord_x[0])
    coord_y.append(coord_y[0])

    print(solution())