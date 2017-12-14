class Yahtzee:

	def singledigits(dice, num):
		score = 0
		for i in dice:
			if i == int(num):
				score += int(num)
			return score

	def threeofakind(dice):
		score = 0
		for i in dice:
			if dice.count(i) >= 3:
				score = sum(dice)
				return score
			else:
				return score

	def fourofakind(dice):
		score = 0
		for i in dice:
			if dice.count(i) >= 4:
				score = sum(dice)
				return score
			else:
				return score

	# def fullhouse(dice):
	# 	score = 0
	# 	if 

	def smallstraight(dice):
		score = 0
		dice = str(sorted(dice))
		if '1, 2, 3, 4' or '2, 3, 4, 5' or '3, 4, 5, 6' in dice:
			score = 30
			return score

	def largestraight(dice):
		score = 0
		dice = str(sorted(dice))
		if '1, 2, 3, 4, 5' or '2, 3, 4, 5, 6' in dice:
			score = 40
			return score

	def yahtzee(dice):
		score = 0
		for i in dice:
			if dice.count(i) == 5:
				score = 50
				return score
			else:
				return score

	def chance(dice):
		score = sum(dice)
		return score













