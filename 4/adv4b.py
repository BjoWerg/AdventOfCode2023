card_count = 0
cards =[]
card_number = -1
with open('input4.txt') as input:
	for line in input:
		# add original card
		card_number +=1
		if card_number < len(cards):
			cards[card_number] += 1
		else:
			cards.append(1)

		# find number of wins for current card
		[card, data] = line.split(':')
		[win_numbers,my_numers] = line.split('|')
		wins = 0
		for w in win_numbers.split():
			for m in my_numers.split():
				if w == m:
					wins += 1
					break
		
		# add cards won
		for i in range(card_number+1, card_number+1+wins):
			if i < len(cards):
				cards[i] += cards[card_number]
			else:
				cards.append(cards[card_number])
		
		card_count += cards[card_number]

print("A total of "+str(card_count)+" cards")

