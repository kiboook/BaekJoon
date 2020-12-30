def search(i, j, visitNode, visitCol):
	global res

	if i == (n - 1):
		res += 1
		return

	for col in range(n):
		if abs(j - col) >= 2 and col not in visitCol:
			check = 0
			for cur in visitNode:
				if abs(cur[0] - (i + 1)) == abs(cur[1] - col):
					check = 1
					break

			if check == 0:
				visitNode.append([i, j])
				visitCol.append(j)
				search(i + 1, col, visitNode, visitCol)
				visitNode.pop()
				visitCol.pop()
		else:
			continue


res = 0
n = int(input())
visitNode = []
visitCol = []

for j in range(n):
	search(0, j, visitNode, visitCol)

print(res)