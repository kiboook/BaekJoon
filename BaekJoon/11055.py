def solution():
    dp = [val for val in arr]

    for i in range(N):
        for j in range(i, -1, -1):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + arr[i])

    return max(dp)


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    print(solution())