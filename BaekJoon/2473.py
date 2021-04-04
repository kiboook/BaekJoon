def solution():
    answer = [float('inf'), 0, 0, 0]

    for i in range(N - 2):
        start, end = i + 1, N - 1

        while start != end:
            total = arr[i] + arr[start] + arr[end]

            if abs(total) < abs(answer[0]):
                answer = [total, i, start, end]

            if total < 0:
                start += 1
            elif total > 0:
                end -= 1
            else:
                print(f"{arr[i]} {arr[start]} {arr[end]}")
                exit(0)

    print(f"{arr[answer[1]]} {arr[answer[2]]} {arr[answer[3]]}")
    exit(0)


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    solution()

# 9
# -120 -30 -7 -4 -2 6 10 18 20

# 9
# -120 -30 -6 -4 -1 6 11 18 20