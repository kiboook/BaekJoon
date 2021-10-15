def solution(app_cnt, need_memory, use_memory_arr, reload_cost_arr):
    answer = 0
    dp_arr = [[0 for _ in range(sum(reload_cost_arr) + 1)] for _ in range(app_cnt + 1)]

    dp_i = 1
    for memory, cost in zip(use_memory_arr, reload_cost_arr):
        for dp_j in range(sum(reload_cost_arr) + 1):
            if cost <= dp_j:
                dp_arr[dp_i][dp_j] = max(dp_arr[dp_i - 1][dp_j], dp_arr[dp_i - 1][dp_j - cost] + memory)
            else:
                dp_arr[dp_i][dp_j] = dp_arr[dp_i - 1][dp_j]
            if dp_arr[dp_i][dp_j] >= need_memory:
                answer = dp_j
                break
        dp_i += 1

    return answer


if __name__ == "__main__":
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(solution(N, M, A, B))

# 5 60
# 30 10 20 35 40
# 3 0 3 5 4

# 6 100
# 30 10 20 35 65 40
# 3 0 3 5 5 4