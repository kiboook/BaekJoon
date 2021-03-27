def solution():
    answer = float('inf')
    start, end, total = 0, 0, 0

    while True:
        if total >= S:
            answer = min(answer, end - start)
            total -= arr[start]
            start += 1

        elif end == N:
            break

        else:
            total += arr[end]
            end += 1

    if answer == float('inf'):
        return 0
    else:
        return answer


if __name__ == "__main__":
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    print(solution())