input = open('input5.txt', 'r')
seeds = []
for s in input.readline().split(':')[1].split():
	seeds.append(int(s))

input.readline()
input.readline()

while True:
	print(seeds)
	maps =[]
	line = input.readline()
	while len(line) > 1:
		map = []
		for m in line.split():
			map.append(int(m))
		maps.append(map)
		line = input.readline()

	for s in range(0,len(seeds)):
		for map in maps:
			if seeds[s] >= map[1] and seeds[s] < (map[1]+map[2]):
				seeds[s] = map[0]+(seeds[s]-map[1])
				break
	
	if not input.readline():
		break
low = seeds[0]
for s in seeds:
	if s < low:
		low = s

print(low)
	