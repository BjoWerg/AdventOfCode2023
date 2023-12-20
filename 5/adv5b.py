input_data = open('input5.txt', 'r')
ranges_in = []
data = input_data.readline().split(':')[1].split()
for i in range(0,len(data),2):
	ranges_in.append([int(data[i]),int(data[i+1])])

input_data.readline()
map_name = input_data.readline()
print("in",ranges_in)
print(map_name)

while True:
	ranges_out = []
	
	maps =[]
	line = input_data.readline()
	while len(line) > 1:
		m = []
		for n in line.split():
			m.append(int(n))
		maps.append(m)
		line = input_data.readline()


	while len(ranges_in) > 0:
		#print("in",ranges_in)
		#print("out",ranges_out)
		#kbd = input('continue')
		r = ranges_in.pop(0)
		#print("range",r)
		handled = False
		for m in maps:
			#print("map",m)
			if r[0] >= m[1] and r[0] < (m[1]+m[2]):
				if (r[0]+r[1]-1) < (m[1]+m[2]):
					ranges_out.append([(m[0]+(r[0]-m[1])), r[1]])
				else:
					ranges_out.append([m[0]+(r[0]-m[1]), m[1]+m[2]-r[0]])
					ranges_in.append([m[1]+m[2], r[0]+r[1]-1-(m[1]+m[2])])
				handled = True
				break
			elif (r[0]+r[1]-1) >= m[1] and (r[0]+r[1]-1) < (m[1]+m[2]):
				ranges_out.append([m[0], r[0]+r[1]-m[1]])
				ranges_in.append([r[0], m[1]-r[0]])
				handled = True
				break
			elif r[0] < m[1] and (r[0]+r[1]-1) >= (m[1]+m[2]):
				ranges_out.append([m[0], m[2]])
				ranges_in.append([r[0], (m[1]-r[0])])
				ranges_in.append([(m[1]+m[2]), (r[0]+r[1]-(m[1]+m[2]))])
				handled = True
				break
		
		if not handled:
			ranges_out.append(r)	
	map_name = input_data.readline()
	if not map_name:
		break
	else:
		for r in ranges_out:
			ranges_in.append(r)
		ranges_out = []
		print("in",ranges_in)
		print(map_name)

print("out",ranges_out)
low = ranges_out[0][0]
for r in ranges_out:
	if r[0] < low:
		low = r[0]

print(low)
