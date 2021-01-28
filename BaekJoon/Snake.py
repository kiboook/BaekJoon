from collections import deque


def solution():
	global arr
	snake_body = deque([[0, 0]])
	snake_dir = deque([[0, 0, 'right']])

	sec = 1
	while True:
		head_loc = []
		snake_head = snake_dir[-1]

		if move_list and int(move_list[0][0]) == sec - 1:  # 방향전환을 해야하는 경우
			if snake_head[2] == 'right':
				if move_list[0][1] == 'D':
					head_loc = [snake_head[0] + 1, snake_head[1], 'down']
				elif move_list[0][1] == 'L':
					head_loc = [snake_head[0] - 1, snake_head[1], 'up']
			elif snake_head[2] == 'down':
				if move_list[0][1] == 'D':
					head_loc = [snake_head[0], snake_head[1] - 1, 'left']
				elif move_list[0][1] == 'L':
					head_loc = [snake_head[0], snake_head[1] + 1, 'right']
			elif snake_head[2] == 'left':
				if move_list[0][1] == 'D':
					head_loc = [snake_head[0] - 1, snake_head[1], 'up']
				elif move_list[0][1] == 'L':
					head_loc = [snake_head[0] + 1, snake_head[1], 'down']
			elif snake_head[2] == 'up':
				if move_list[0][1] == 'D':
					head_loc = [snake_head[0], snake_head[1] + 1, 'right']
				elif move_list[0][1] == 'L':
					head_loc = [snake_head[0], snake_head[1] - 1, 'left']
			move_list.popleft()
		else:  # 직진하는 경우
			if snake_head[2] == 'up':
				head_loc = [snake_head[0] - 1, snake_head[1], 'up']
			elif snake_head[2] == 'right':
				head_loc = [snake_head[0], snake_head[1] + 1, 'right']
			elif snake_head[2] == 'down':
				head_loc = [snake_head[0] + 1, snake_head[1], 'down']
			elif snake_head[2] == 'left':
				head_loc = [snake_head[0], snake_head[1] - 1, 'left']

		if (head_loc[:2] in snake_body or
				head_loc[0] < 0 or head_loc[0] >= arr_size or
				head_loc[1] < 0 or head_loc[1] >= arr_size):
			return sec

		if head_loc[:2] in apple_loc:
			apple_loc.remove(head_loc[:2])
			snake_dir.append(head_loc)
			snake_body.append(head_loc[:2])
		else:
			snake_dir.popleft()
			snake_body.popleft()
			snake_dir.append(head_loc)
			snake_body.append(head_loc[:2])

		sec += 1


if __name__ == '__main__':
	arr_size = int(input())
	arr = [[0] * arr_size for _ in range(arr_size)]

	apple_cnt = int(input())
	apple_loc = [list(map(int, input().rsplit())) for _ in range(apple_cnt)]
	for i in range(apple_cnt):
		apple_loc[i][0] -= 1
		apple_loc[i][1] -= 1

	move_cnt = int(input())
	move_list = deque([list(input().rsplit()) for _ in range(move_cnt)])
	print(solution())