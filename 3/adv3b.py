with open('input3.txt') as indata:
	
	prev = indata.readline().rstrip()
	curr = indata.readline().rstrip()
	nxt = indata.readline().rstrip()

	gears_sum = 0
	line_length = len(curr)

	num_prev = []
	start_prev = []
	stop_prev = []

	# find numbers in current line
	num_curr = []
	start_curr = []
	stop_curr = []
	number_found = False
	for i in range(0, line_length):
		if curr[i].isdigit():
			if number_found:
				# add to number
				number += curr[i]
			else:
				# new number found
				number = curr[i]
				number_found = True
				start_curr.append(i)
		else:
			if number_found:
				# add to num_list
				num_curr.append(number)
				stop_curr.append(i-1)
				number_found = False	
	if number_found:
		# add to num_list
		num_curr.append(number)
		stop_curr.append(i)
				
	while True:
		# find numbers in next line
		num_nxt = []
		start_nxt = []
		stop_nxt = []
		number_found = False
		for i in range(0, line_length):
			if nxt[i].isdigit():
				if number_found:
					# add to number
					number += nxt[i]
				else:
					# new number found
					number = nxt[i]
					number_found = True
					start_nxt.append(i)

			else:
				if number_found:
					# add to num_list
					num_nxt.append(number)
					stop_nxt.append(i-1)
					number_found = False
		if number_found:
			# add to num_list
			num_nxt.append(number)
			stop_nxt.append(i)

		# find gears
		for i in range(0, line_length):
			if curr[i] == '*':
				# find corresponding numbers in current line
				num_gears = []
				# find numbers adjecent to gear in prev
				for n in range(0,len(num_prev)):
					if start_prev[n] <= i+1 and stop_prev[n] >= i-1:
						num_gears.append(num_prev[n])
				# find numbers adjecent to gear in curr
				for n in range(0,len(num_curr)):
					if start_curr[n] == i+1 or stop_curr[n] == i-1:
						num_gears.append(num_curr[n])
				# find numbers adjecent to gear in nxt
				for n in range(0,len(num_nxt)):
					if start_nxt[n] <= i+1 and stop_nxt[n] >= i-1:
						num_gears.append(num_nxt[n])

				if len(num_gears) == 2:
					gears_sum += int(num_gears[0])*int(num_gears[1])
		
		# prepare for next line
		num_prev = num_curr
		start_prev = start_curr
		stop_prev = stop_curr
		prev = curr
		
		num_curr = num_nxt
		start_curr = start_nxt
		stop_curr = stop_nxt
		curr = nxt
		
		nxt = indata.readline().rstrip()
		
		if not nxt:
			break

print(gears_sum)

