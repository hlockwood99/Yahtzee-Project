from dice import Dice
import Yahtzee
import random

response = input('Hi there, friend! Would you like to play Yahtzee? [y] or [n]')
while response != 'y' and response != 'n':
	print('Try again. Please type [y] or [n]')
	response = input('Hi there, friend! Would you like to play Yahtzee? [y] or [n]')
	if response == 'y':
		Dice()
	elif response == 'n':
		print('Come again soon!')
		break

for i in range 13:
	dice = []
	try1 = input('Would you like to roll the dice? (Try 1 - you pass your turn)')
	while response != 'y' and response != 'n':
		print('Try again. Please type [y] or [n]')
		try1 = input('Would you like to roll the dice? (Try 1 - you pass your turn)')
		if response == 'y':
			dice = roll.DiceRoll()
		elif response == 'n':
			print('Calculating score... ')
			score = Yahtzeetool.singledigits(dice) + Yahtzeetool.threeofakind(dice) + Yahtzeetool.fourofakind(dice)
			+ Yahtzeetool.fullhouse(dice) + Yahtzeetool.smallstraight(dice) + Yahtzeetool.largestraight(dice)
			+ Yahtzeetool.yahtzee(dice) + Yahtzeetool.chance(dice)
			finalscore.append(score)
			continue

	try2 = input('Would you like to reroll the dice? (Try 2) ')
	while response != 'y' and response != 'n':
		print('Try again. Please type [y] or [n]')
		try2 = input('Would you like to reroll the dice? (Try 2) ')
		if response == 'y':
			roll.DiceRoll()
		elif response == 'n':
			print('Calculating score... ')
			score = Yahtzeetool.singledigits(dice) + Yahtzeetool.threeofakind(dice) + Yahtzeetool.fourofakind(dice)
			+ Yahtzeetool.fullhouse(dice) + Yahtzeetool.smallstraight(dice) + Yahtzeetool.largestraight(dice)
			+ Yahtzeetool.yahtzee(dice) + Yahtzeetool.chance(dice)
			finalscore.append(score)
			continue

	try3 = input('Would you like to reroll the dice? (Try 3) ')
	while response != 'y' and response != 'n':
		print('Try again. Please type [y] or [n]')
		try3 = input('Would you like to reroll the dice? (Try 3) ')
		if response == 'y':
			roll.DiceRoll()
		elif response == 'n':
			print('Calculating score... ')
			score = Yahtzeetool.singledigits(dice) + Yahtzeetool.threeofakind(dice) + Yahtzeetool.fourofakind(dice)
			+ Yahtzeetool.fullhouse(dice) + Yahtzeetool.smallstraight(dice) + Yahtzeetool.largestraight(dice)
			+ Yahtzeetool.yahtzee(dice) + Yahtzeetool.chance(dice)
			finalscore.append(score)
			continue


Yahtzeetool = Yahtzee()
roll = Dice()
finalscore = []

print('FINAL SCORE: ' + finalscore)