def solution(score):
	if sum(score[:(len(score) // 2)]) == sum(score[(len(score) // 2):]):
		return "LUCKY"
	else:
		return "READY"


if __name__ == "__main__":
	score = list(map(int, input()))
	print(solution(score))