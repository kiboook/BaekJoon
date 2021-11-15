def solution(n):
    # n 보다 작거나 같은 제곱수의 값 + 1
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1

    for i in range(2, n + 1):
        output = float('inf')
        j = 1
        while (j ** 2) <= i:
            output = min(output, dp[i - (j ** 2)])
            j += 1
        dp[i] = output + 1

    return dp[n]


if __name__ == "__main__":
    print(solution(int(input())))