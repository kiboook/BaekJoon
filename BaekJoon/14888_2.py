def DFS(arr, step, output, plus, minus, mul, divide):
    global max_output, min_output

    if step == n - 1:
        max_output = max(max_output, output)
        min_output = min(min_output, output)
        return

    if plus:
        DFS(arr, step + 1, output + arr[step + 1], plus - 1, minus, mul, divide)
    if minus:
        DFS(arr, step + 1, output - arr[step + 1], plus, minus - 1, mul, divide)
    if mul:
        DFS(arr, step + 1, output * arr[step + 1], plus, minus, mul - 1, divide)
    if divide:
        DFS(arr, step + 1, int(output / arr[step + 1]), plus, minus, mul, divide - 1)


def solution(arr, operator):

    DFS(arr, 0, arr[0], operator[0], operator[1], operator[2], operator[3])

    print(max_output)
    print(min_output)

    return


if __name__ == "__main__":
    max_output = float('-inf')
    min_output = float('inf')

    n = int(input())
    arr = list(map(int, input().split()))
    operator = list(map(int, input().split()))

    solution(arr, operator)