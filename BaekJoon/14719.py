def solution(arr):
    answer = 0
    left_cur, right_cur = 0, len(arr) - 1

    left_wall, right_wall = arr[left_cur], arr[right_cur]
    while left_cur <= right_cur:
        left_wall = max(left_wall, arr[left_cur])
        right_wall = max(right_wall, arr[right_cur])

        if left_wall <= right_wall:
            answer += left_wall - arr[left_cur]
            left_cur += 1
        else:
            answer += right_wall - arr[right_cur]
            right_cur -= 1

    return answer


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    print(solution(arr))