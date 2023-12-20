from enum import Enum

Card = Enum('Card', ['J','2','3','4','5','6','7','8','9','T','Q','K','A'])

def hand_cmp(hand1,hand2):
	res = 0
	for i in range(0,len(hand1[0])):
		if Card[hand1[0][i]].value > Card[hand2[0][i]].value:
			res = 1
			break
		elif Card[hand1[0][i]].value < Card[hand2[0][i]].value:
			res = -1
			break
	return res

high_hands = []
one_hands = []
two_hands = []
three_hands = []
house_hands = []
four_hands = []
five_hands = []

with open('input7.txt') as hand_list:
	for h in hand_list:
		[hand, bet] = h.split()
		
		card_count = []
		for c in Card:
			card_count.append(hand.count(c.name))
		knight = card_count.pop(0)
		if ( (5 in card_count) or
			 (knight == 5) or
			 (4 in card_count and knight == 1) or
			 (3 in card_count and knight == 2) or
			 (2 in card_count and knight == 3) or
			 (knight == 4) ):
			five_hands.append([hand, bet])
		elif ( (4 in card_count) or 
			   (3 in card_count and knight == 1) or 
			   (2 in card_count and knight == 2) or 
			   (knight == 3) ):
			four_hands.append([hand, bet])
		elif ( (3 in card_count and 2 in card_count) or
			   (2 == card_count.count(2) and knight == 1) ):
			house_hands.append([hand, bet])
		elif ( (3 in card_count) or
			   (2 in card_count and knight == 1) or 
			   (knight == 2) ):
			three_hands.append([hand, bet])
		elif 2 == card_count.count(2):
			two_hands.append([hand, bet])
		elif ( (2 in card_count) or
			   (knight == 1) ):
			one_hands.append([hand, bet])
		else:
			high_hands.append([hand, bet])
		

total_winnings = 0
count = 0
for h in sorted(high_hands, cmp=hand_cmp):
	count += 1
	total_winnings += count*int(h[1])

for h in sorted(one_hands, cmp=hand_cmp):
	count += 1
	total_winnings += count*int(h[1])

for h in sorted(two_hands, cmp=hand_cmp):
	count += 1
	total_winnings += count*int(h[1])

for h in sorted(three_hands, cmp=hand_cmp):
	count += 1
	total_winnings += count*int(h[1])

for h in sorted(house_hands, cmp=hand_cmp):
	count += 1
	total_winnings += count*int(h[1])

for h in sorted(four_hands,cmp=hand_cmp):
	count += 1
	total_winnings += count*int(h[1])

for h in sorted(five_hands, cmp=hand_cmp):
	count += 1
	total_winnings += count*int(h[1])

print(total_winnings)