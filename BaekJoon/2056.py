import sys


def solution():
    for i in range(1, N + 1):
        info = list(map(int, sys.stdin.readline().rsplit()))
        infos.append(info)
        work[i] = info[0]

    for idx, info in enumerate(infos):
        if info[1] >= 1:
            hard_work = 0
            pre_works = info[2:]
            for pre_work in pre_works:
                hard_work = max(hard_work, work[pre_work])
            work[idx + 1] += hard_work

    return max(work)


if __name__ == "__main__":
    N = int(input())
    work = [0] * (N + 1)
    infos = []

    print(solution())