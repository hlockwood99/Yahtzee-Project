#Yahtzee class: checks the conditions
class Yahtzee:

	#Count and add only a certain number, such as three twos
	def singledigits(dice, num):
		score = 0
		for i in dice:
			if i == int(num):
				score += int(num)
			return score

	#Three kinds of the same dice
	def threeofakind(dice):
		score = 0
		for i in dice:
			if dice.count(i) >= 3:
				score = sum(dice)
				return score
			else:
				return score

	#Four kinds of the same dice
	def fourofakind(dice):
		score = 0
		for i in dice:
			if dice.count(i) >= 4:
				score = sum(dice)
				return score
			else:
				return score

	#Full house where there are two of the same number and 3 of the same number 
	#(but different from the two of the same number)
	def fullhouse(dice):
		score = 0
		temp = []
		for i in dice:
			temp.append(i)
			temp.sort()
		if temp[0] == temp[1] and temp[2] == temp[3] and temp[3] == temp[4]:
			score = 25
			return score
		elif temp[0] == temp[1] and temp[1] == temp[2] and temp[3] == temp[4]:
			score = 25
			return score
		else:
			return score

	#A small straight
	def smallstraight(dice):
		score = 0
		dice = str(sorted(dice))
		if '1, 2, 3, 4' or '2, 3, 4, 5' or '3, 4, 5, 6' in dice:
			score = 30
			return score

	#A large straight
	def largestraight(dice):
		score = 0
		dice = str(sorted(dice))
		if '1, 2, 3, 4, 5' or '2, 3, 4, 5, 6' in dice:
			score = 40
			return score

	#Five of the same dice (Yahtzee)
	def yahtzee(dice):
		score = 0
		for i in dice:
			if dice.count(i) == 5:
				score = 50
				return score
			else:
				return score

	#Score total of all 5 Dice
	def chance(dice):
		score = sum(dice)
		return score




