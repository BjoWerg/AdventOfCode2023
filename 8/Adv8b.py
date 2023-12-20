import re
import math

in_data = open('input8.txt', 'r')

direction = in_data.readline().rstrip()
in_data.readline()
left = {}
right = {}

node_list = []
end_count = []
node = in_data.readline()
while node:
	[key, L, R] = re.findall(r'([A-Z]{3})',node)
	left[key] = L
	right[key] = R
	if key[-1] == 'A':
		node_list.append(key)
		end_count.append(0)
	node = in_data.readline()

done = False
count = 0
while not done:
	if  direction[count%len(direction)] == 'L':
		count += 1
		for i in range(0,len(node_list)):
			node_list[i] = left[node_list[i]]
			if node_list[i][-1] == 'Z' and end_count[i] == 0:
				end_count[i] = count
	else:
		count += 1
		for i in range(0,len(node_list)):
			node_list[i] = right[node_list[i]]
			if node_list[i][-1] == 'Z' and end_count[i] == 0:
				end_count[i] = count

	if not 0 in end_count:
		done = True
ans = 1
for c in end_count:
	ans = math.lcm(ans,c)

print(ans)		
	