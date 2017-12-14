def singledigits(dice, num):
	score = 0
	for i in dice:
		if i == int(num):
			score += int(num)
		return score

def threeofakind(dice):
	score = 0
	for i in dice:
		if if dice.count(i) >= 3:
			score = sum(dice)
			return score
		else:
			return score
