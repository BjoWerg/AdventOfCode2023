import re

in_data = open('input8.txt', 'r')

direction = in_data.readline().rstrip()
in_data.readline()
left = {}
right = {}

node = in_data.readline()
while node:
	[key, L, R] = re.findall(r'([A-Z]{3})',node)
	left[key] = L
	right[key] = R
	node = in_data.readline()

next_node = 'AAA'
count = 0
while not next_node == 'ZZZ':
	if direction[count%len(direction)] == 'L':
		next_node = left[next_node]
	else:
		next_node = right[next_node]
	count += 1

print(count)		
	