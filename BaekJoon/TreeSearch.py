import sys
from string import ascii_uppercase


def preOrder(root):
	if root is None:
		return

	print(root, end='')
	preOrder(tree[root][0])
	preOrder(tree[root][1])


def inOrder(root):
	if root is None:
		return

	inOrder(tree[root][0])
	print(root, end='')    #  DBAECFG  BDACEFG
	inOrder(tree[root][1])


def postOrder(root):
	if root is None:
		return

	postOrder(tree[root][0])
	postOrder(tree[root][1])
	print(root, end='')


alpha = ascii_uppercase
node_num = int(input())
tree = {alpha[i]: [] for i in range(node_num)}

for _ in range(node_num):
	parent, left, right = sys.stdin.readline().rsplit()

	if left == '.':
		tree[parent].append(None)
	else:
		tree[parent].append(left)

	if right == '.':
		tree[parent].append(None)
	else:
		tree[parent].append(right)

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')