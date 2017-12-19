from dice import Dice
import Yahtzee
import random

#Asking the user if he or she would like to play Yahtzee! Includes error checking.
response = input('Hi there, friend! Would you like to play Yahtzee? [y] or [n]')
while response != 'y' and response != 'n':
	print('Try again. Please type [y] or [n]')
	response = input('Hi there, friend! Would you like to play Yahtzee? [y] or [n]')
	if response == 'y':
		break
	elif response == 'n':
		print('Come again soon!')
		quit()

Yahtzeetool = Yahtzee()
roll = Dice()

#The player plays thirteen rounds, like in the actual game.
for i in range 13:
	#Making two lists. "dice" contains the dice values. 
	dice = []
	#"finalscores" would contain the final score of a single round.
	finalscores = []
	try1 = input('Would you like to roll the dice? [y] or [n] (Try 1 - if [n], you pass your turn)')
	while response != 'y' and response != 'n':
		print('Try again. Please type [y] or [n]')
		try1 = input('Would you like to roll the dice? [y] or [n] (Try 1 - if [n], you pass your turn)')
		#if yes, the code will generate 5 random numbers.
		if response == 'y':
			dice = roll.DiceRoll()
		#if no, the code will check the values in "dice" to see if they meets certain
		#conditions, such as "fullhouse." Of course, since it is the first round, it
		#is similar to a player making a pass.
		elif response == 'n':
			print('Calculating score... ')
			#Adds up the scores that satisfy certain conditions.
			score = Yahtzeetool.singledigits(dice) + Yahtzeetool.threeofakind(dice) + Yahtzeetool.fourofakind(dice)
			+ Yahtzeetool.fullhouse(dice) + Yahtzeetool.smallstraight(dice) + Yahtzeetool.largestraight(dice)
			+ Yahtzeetool.yahtzee(dice) + Yahtzeetool.chance(dice)
			finalscore.append(score)
			#Go back to round 1
			continue

	try2 = input('Would you like to reroll the dice? [y] or [n] (Try 2) ')
	while response != 'y' and response != 'n':
		print('Try again. Please type [y] or [n]')
		try2 = input('Would you like to reroll the dice? [y] or [n] (Try 2) ')
		#Similar to try 1, but this time only certain values the player chooses to reroll
		#will be rolled.
		if response == 'y':
			roll.DiceRoll()
		#If no, the code will check what conditions the values in "dice" meets, such as 
		#full house.
		elif response == 'n':
			print('Calculating score... ')
			#Adds up the scores that satisfy certain conditions.
			score = Yahtzeetool.singledigits(dice) + Yahtzeetool.threeofakind(dice) + Yahtzeetool.fourofakind(dice)
			+ Yahtzeetool.fullhouse(dice) + Yahtzeetool.smallstraight(dice) + Yahtzeetool.largestraight(dice)
			+ Yahtzeetool.yahtzee(dice) + Yahtzeetool.chance(dice)
			finalscore.append(score)
			#Go back to round 1
			continue

	try3 = input('Would you like to reroll the dice? [y] or [n] (Try 3) ')
	while response != 'y' and response != 'n':
		print('Try again. Please type [y] or [n]')
		try3 = input('Would you like to reroll the dice? [y] or [n] (Try 3) ')
		if response == 'y':
			roll.DiceRoll()
		elif response == 'n':
			print('Calculating score... ')
			#Adds up the scores that satisfy certain conditions.
			score = Yahtzeetool.singledigits(dice) + Yahtzeetool.threeofakind(dice) + Yahtzeetool.fourofakind(dice)
			+ Yahtzeetool.fullhouse(dice) + Yahtzeetool.smallstraight(dice) + Yahtzeetool.largestraight(dice)
			+ Yahtzeetool.yahtzee(dice) + Yahtzeetool.chance(dice)
			finalscore.append(score)
			#Automatically goes back to round 1

totalscore = sum(finalscores)
print('FINAL SCORE: ' + totalscore)






