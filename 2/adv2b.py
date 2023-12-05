sum = 0
colors = ["red","green","blue"]

with open('input2.txt') as input:
	for line in input:
		[game,data] = line.split(':')
		minimum = [0,0,0]
		
		for draws in data.split(';'):
			for cube in draws.split(','):
				[n, c] = cube.split()
				if int(n) > minimum[colors.index(c)]:
					minimum[colors.index(c)] = int(n)
		
		sum += minimum[0]*minimum[1]*minimum[2]

print(sum)

