from itertools import combinations
import sys


def DFS(candidate_idx):
    visit = [[0 for _ in range(5)] for _ in range(5)]
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    stack = [candidate_idx[0]]

    while stack:
        now_i, now_j = stack.pop()
        for value in dirs:
            visit_i, visit_j = now_i + value[0], now_j + value[1]
            if 0 <= visit_i < 5 and 0 <= visit_j < 5 and not visit[visit_i][visit_j]:
                if [visit_i, visit_j] in candidate_idx:
                    stack.append([visit_i, visit_j])
                    visit[visit_i][visit_j] = 1

    if sum(sum(visit, [])) == 7:
        return True
    else:
        return False


def is_seven_princess(princessCandidate):
    yCnt = 0
    candidate_idx = []
    for idx in princessCandidate:
        # 4. 숫자를 5로 나눈 몫과 나머지를 통해 배열 인덱스를 알 수 있다.
        i, j = idx // 5, idx % 5
        if students[i][j] == 'Y':
            yCnt += 1
        candidate_idx.append([idx // 5, idx % 5])

    # 5. 임도연파가 4명 이상이라면 칠공주를 구성할 수 없다.
    if yCnt >= 4:
        return False
    else:
        # 6. 임도연파가 3명 이하라면 모두 가로 세로로 붙어있는지 확인한다.
        if DFS(candidate_idx):
            return True
        else:
            return False


def solution():
    answer = 0
    # 2. 25중 7명을 선택한다.
    princessCandidates = combinations([i for i in range(25)], 7)
    for princessCandidate in princessCandidates:
        # 3. 칠공주파를 구성할 수 있는지 확인한다.
        if is_seven_princess(princessCandidate):
            answer += 1
    return answer


if __name__ == "__main__":
    # 1. 25명중 7명을 선택 후 그 7명이 칠공주가 될 수 있는지 파악한다.
    students = [list(sys.stdin.readline()) for _ in range(5)]
    print(solution())