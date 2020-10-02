import sys


my_set = set()
for _ in range(int(input())):
    order = sys.stdin.readline().rsplit()
    
    if order[0] == 'add':
        my_set.add(int(order[1]))
    elif order[0] == 'remove':
        if int(order[1]) in my_set:
            my_set.remove(int(order[1]))
    elif order[0] == 'check':
        if int(order[1]) in my_set:
            print(1)
        else:
            print(0)
    elif order[0] == 'toggle':
        if int(order[1]) in my_set:
            my_set.remove(int(order[1]))
        else:
            my_set.add(int(order[1]))
    elif order[0] == 'all':
        my_set = set(range(1, 21))
    elif order[0] == 'empty':
        my_set.clear()


# 26
# add 1
# add 2
# check 1
# check 2
# check 3
# remove 2
# check 1
# check 2
# toggle 3
# check 1
# check 2
# check 3
# check 4
# all
# check 10
# check 20
# toggle 10
# remove 20
# check 10
# check 20
# empty
# check 1
# toggle 1
# check 1
# toggle 1
# check 1