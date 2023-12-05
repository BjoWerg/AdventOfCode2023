with open('input3.txt') as indata:
	
	prev = indata.readline().rstrip()
	curr = indata.readline().rstrip()
	nxt = indata.readline().rstrip()
	#print(prev)
	#print(curr)
	#print(nxt)

	part_sum = 0
	line_length = len(curr)

	while True:

		number_found = False
		part_found = False

		for i in range(0, line_length):
			if curr[i].isdigit():
				if number_found:
					# add to number
					number += curr[i]
				else:
					# new number found
					number = curr[i]
					number_found = True
					part_found = False

				if number_found and not part_found:
					#check for symbol
					if i > 0 and not prev[i-1].isdigit() and not prev[i-1] == '.':
						part_found = True
					if not prev[i].isdigit() and not prev[i] == '.':
						part_found = True
					if i < (line_length-1) and not prev[i+1].isdigit() and not prev[i+1] == '.':
						part_found = True

					if i > 0 and not curr[i-1].isdigit() and not curr[i-1] == '.':
						part_found = True
					if i < (line_length-1) and not curr[i+1].isdigit() and not curr[i+1] == '.':
						part_found = True

					if i > 0 and not nxt[i-1].isdigit() and not nxt[i-1] == '.':
						part_found = True
					if not nxt[i].isdigit() and not nxt[i] == '.':
						part_found = True
					if i < (line_length-1) and not nxt[i+1].isdigit() and not nxt[i+1] == '.':
						part_found = True

			else:
				if number_found:
					# end of number found, check for symbol
					if not prev[i].isdigit() and not prev[i] == '.':
						part_found = True
					if not curr[i].isdigit() and not curr[i] == '.':
						part_found = True
					if not nxt[i].isdigit() and not nxt[i] == '.':
						part_found = True
					
					if part_found:
						part_sum += int(number)
						#print(number)
					
					number_found = False
					part_found = False
			
		if part_found:
			part_sum += int(number)
			#print(number)
		
		#key = input("Continue!")
		
		# prepare next line
		prev = curr
		curr = nxt
		nxt = indata.readline().rstrip()
		
		if not nxt:
			break

		#print(prev)
		#print(curr)
		#print(nxt)

print(part_sum)

