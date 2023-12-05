sum = 0

with open('input1.txt') as input:
	for line in input:
		digits = list(filter(lambda d: d.isdigit(), line))
		sum += int(digits[0]+digits[-1])
				
print(sum)

