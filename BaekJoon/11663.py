import sys


def calc_point(line_start, line_end):

    start = 0
    end = len(point) - 1
    while start <= end:
        left = (start + end) // 2
        if line_start <= point[left] <= line_end:
            end = left - 1
        else:
            if point[left] < line_start:
                start = left + 1
            elif point[left] > line_end:
                end = left - 1

    start = 0
    end = len(point) - 1
    while start <= end:
        right = (start + end) // 2
        if line_start <= point[right] <= line_end:
            start = right + 1
        else:
            if point[right] < line_start:
                start = right + 1
            elif point[right] > line_end:
                end = right - 1

    if point[left] >= line_start and point[right] <= line_end:
        return right - left + 1
    if point[left] < line_start and point[right] > line_end:
        return right - left - 1

    return right - left


def solution():
    for line in lines:
        print(calc_point(line[0], line[1]))


if __name__ == "__main__":
    N, M = map(int, input().split())
    point = list(map(int, input().split()))
    point.sort()
    lines = []
    for _ in range(M):
        line = tuple(map(int, sys.stdin.readline().rsplit()))
        lines.append(line)

    solution()