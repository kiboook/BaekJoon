import collections


n = int(input())
my_card = list(map(int, input().split()))

m = int(input())
find_card = list(map(int, input().split()))

my_card = collections.Counter(my_card)

for num in find_card:
	try:
		print(my_card[num], end=' ')
	except KeyError:
		print(0, end=' ')