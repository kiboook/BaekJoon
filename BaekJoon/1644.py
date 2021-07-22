def make_prime_number(input_data):
    prefix_sum_prime_number_bowl = [0]
    nums = [True for _ in range(input_data + 1)]
    nums[0] = False
    nums[1] = False

    # 1. 에라토스테네스의 체를 이용하여 소수를 구하고 구간합을 저장한다.
    for num in range(input_data + 1):
        if nums[num]:
            prefix_sum_prime_number_bowl.append(prefix_sum_prime_number_bowl[-1] + num)
            product = 2
            while num * product <= input_data:
                nums[num * product] = False
                product += 1

    return prefix_sum_prime_number_bowl


def solution():
    answer = 0
    input_data = int(input())
    prefix_sum_prime_numbers = make_prime_number(input_data)

    # 2. 투포인터로 구간합을 탐색해 연속합이 답이 되는 경우를 찾는다.
    left = right = 0
    while right < len(prefix_sum_prime_numbers):
        check = prefix_sum_prime_numbers[right] - prefix_sum_prime_numbers[left]
        if check == input_data:
            answer += 1
            right += 1
        elif check < input_data:
            right += 1
        else:
            left += 1

    return answer


if __name__ == "__main__":
    print(solution())