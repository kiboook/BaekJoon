def candidating_nums(i, j):
    nums = {num: True for num in range(10)}

    for k in range(9):
        nums[sudoku[i][k]] = False
        nums[sudoku[k][j]] = False

    for x in range((i // 3) * 3, (i // 3) * 3 + 3):
        for y in range((j // 3) * 3, (j // 3) * 3 + 3):
            nums[sudoku[x][y]] = False

    return nums


def DFS(count, loop, zero_pos):
    global sudoku

    if count == loop:
        for row in sudoku:
            print(''.join(map(str, row)))
        exit(0)

    i, j = zero_pos[count]
    candidate = candidating_nums(i, j)

    for num in candidate:
        if candidate[num]:
            sudoku[i][j] = num
            DFS(count + 1, loop, zero_pos)
            sudoku[i][j] = 0


def solution():
    zero_pos = []

    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                zero_pos.append([i, j])

    loop = len(zero_pos)
    DFS(0, loop, zero_pos)


if __name__ == "__main__":
    sudoku = [list(map(int, input())) for _ in range(9)]

    solution()

