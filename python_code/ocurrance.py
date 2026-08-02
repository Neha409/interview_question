from collections import Counter

st = "aaabbcctdde"

counter = Counter(st)

print(counter)

for i,count in counter.items():
	if count == 1:
		print(i)
		break