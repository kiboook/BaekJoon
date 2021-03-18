import sys
from collections import deque
from copy import deepcopy
from itertools import combinations


# 적들이 아래로 이동하는 함수
def move_enemy(field):
    row = [0] * M
    field.appendleft(row)
    field.pop()


# 궁수가 쏠 위치를 정하는 함수
def choice_attack_location(field, arrow):
    all_attack_location = list()
    for i in range(N):
        for j in range(M):
            distance = abs(arrow[0] - i) + abs(arrow[1] - j)
            if distance <= D and field[i][j] == 1:
                all_attack_location.append((distance, i, j))

    all_attack_location.sort(key=lambda x: (x[0], x[2]))
    if all_attack_location:
        return True, all_attack_location[0]
    else:
        return False, None


# 세 명의 궁수가 쏠 위치를 저장하는 함수
def init_attack_location(field, arrows):
    attack_location = list()
    for arrow in arrows:
        arrow_attack_loc_check = choice_attack_location(field, arrow)
        if arrow_attack_loc_check[0]:
            attack_location.append(arrow_attack_loc_check[1])

    if attack_location:
        return set(attack_location)

    return attack_location


def defense(field, arrows):
    kill = 0

    # 적이 없어질 때 까지 반복
    while sum(sum(field, [])) != 0:

        # 세 명의 궁수가 쏠 위치 저장
        attack_location = init_attack_location(field, arrows)

        # 공격
        for attack in attack_location:
            if field[attack[1]][attack[2]] == 1:
                kill += 1
                field[attack[1]][attack[2]] = 0

        # 적들 아래로 이동
        move_enemy(field)

    return kill


def solution():
    answer = -float('inf')
    arrows = [(N, i) for i in range(M)]

    for value in combinations(arrows, 3):
        answer = max(answer, defense(deepcopy(field), value))

    return answer


if __name__ == "__main__":
    N, M, D = map(int, input().split())
    field = deque([list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)])

    print(solution())