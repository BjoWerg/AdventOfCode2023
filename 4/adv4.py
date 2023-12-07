point_sum = 0

with open('input4.txt') as input:
	for line in input:
		[card, data] = line.split(':')
		[win_numbers,my_numers] = line.split('|')
		
		points = 0
		for w in win_numbers.split():
			for n in my_numers.split():
				if w == n:
					if points == 0:
						points = 1
					else:
						points *= 2
					break
				
		point_sum += points
		print(card+" has "+str(points)+", total: "+str(point_sum))

print("A total of "+str(point_sum)+" for all cards")

