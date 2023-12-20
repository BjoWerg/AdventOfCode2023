input_data = open('input6.txt', 'r')
time = []
for t in  input_data.readline().split(':')[1].split():
	time.append(int(t))
dist = []
for d in input_data.readline().split(':')[1].split():
	dist.append(int(d))

tot_margin = 1
for i in range(0, len(time)):
	margin = 0
	for t in range(1,time[i]):
		if t*(time[i]-t) > dist[i]:
			margin +=1
	tot_margin *= margin
print(tot_margin)