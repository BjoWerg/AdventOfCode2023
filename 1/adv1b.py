sum = 0
digit_words = ["one","two","three","four","five","six","seven","eight","nine"]



with open('input1.txt') as input:
	for line in input:
		first = "x"
		last = "x"
		for i in range(0,len(line)):
			if line[i].isdigit() and first == "x":
				first = line[i]
			else:
				for dw in digit_words:
					if line.find(dw,0,i+1) >= 0 and first == "x":
						first =  str(digit_words.index(dw)+1)
						
			if line[len(line)-i-1].isdigit() and last == "x":
				last = line[len(line)-i-1]
			else:
				for dw in digit_words:
					if line.find(dw, len(line)-i-1, len(line)) >= 0 and last == "x":
						last = str(digit_words.index(dw)+1)
		sum += int(first+last)
print(sum)

