from string import ascii_lowercase


alpha = dict()
for key in ascii_lowercase:
	alpha[key] = len(alpha) + 1


n = int(input())
my_str = input()
hash_val = 0

for i in range(n):
	hash_val += (alpha[my_str[i]] * (31 ** i))

print(hash_val % 1234567891)