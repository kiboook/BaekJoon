import sys


def solution():
    start, end = 0, N - 1
    answer = [water[start] + water[end], start, end]

    while start != end:
        left = [water[start] + water[end - 1], start, end - 1]
        right = [water[start + 1] + water[end], start + 1, end]

        if abs(left[0]) > abs(right[0]):
            tmp_answer = right
        else:
            tmp_answer = left

        if tmp_answer[1] != tmp_answer[2] and abs(answer[0]) > abs(tmp_answer[0]):
            answer = tmp_answer

        start, end = tmp_answer[1], tmp_answer[2]

    print(water[answer[1]], water[answer[2]])


if __name__ == "__main__":
    N = int(input())
    water = list(map(int, sys.stdin.readline().rsplit()))

    solution()

# 9
# -120 -30 -7 -4 -2 6 10 18 20