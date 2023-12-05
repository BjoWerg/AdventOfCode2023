sum = 0
limit = {"red": 12,"green": 13, "blue": 14}

with open('input2.txt') as input:
	for line in input:
		[game,data] = line.split(':')
		is_possible = True
		
		for draws in data.split(';'):
			for cube in draws.split(','):
				[num, color] = cube.split()
				if int(num) > limit[color]:
					is_possible = False
		
		if is_possible:
			sum += int(game.split()[1])

print(sum)

