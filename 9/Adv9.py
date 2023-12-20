def add_val(il):
	print(il)
	ul = []
	for i in range(1,len(il)):
		ul.append(il[i]-il[i-1])
		
	done = True
	for u in ul:
		if not u == 0:
			done = False
			break

	if done:
		return 0
	else:
		return (ul[-1] + add_val(ul))

sum_of_extr_vals = 0

with open('input9.txt') as in_data:
	for values in in_data:
		il = []
		for v in values.split():
			il.append(int(v))
		extr_value = il[-1] + add_val(il)
		print(extr_value)
		sum_of_extr_vals += extr_value

print(sum_of_extr_vals)