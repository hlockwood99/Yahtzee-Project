from dice import Dice
from yahtzeee import Yahtzee
import random

#Asking the user if he or she would like to play Yahtzee! Includes error checking.
response = input('Hi there, friend! Would you like to play Yahtzee? [y] or [n]' )
while response != 'y' and response != 'n':
	print('Try again. Please type [y] or [n]' )
	response = input('Hi there, friend! Would you like to play Yahtzee? [y] or [n]' )
	if response == 'y':
		break
	elif response == 'n':
		print('Come again soon!')
		quit()

Yahtzeetool = Yahtzee()
roll = Dice()

try2 = input('Would you like to roll the dice? [y] or [n] ')
while try2 != 'y' and try2 != 'n':
	print('Try again. Please type [y] or [n]')
	try2 = input('Would you like to roll the dice? [y] or [n] ')
	#Similar to try 1, but this time only certain values the player chooses to reroll
	#will be rolled.
finalscores = []
if try2 == 'y':
	roll.DiceRoll()
#If no, the code will check what conditions the values in "dice" meets, such as 
#full house.

	print('Calculating score... ')
	#Adds up the scores that satisfy certain conditions.
	score = Yahtzeetool.singledigits(roll.diceRolled) + Yahtzeetool.threeofakind(roll.diceRolled) + Yahtzeetool.fourofakind(roll.diceRolled)+ Yahtzeetool.fullhouse(roll.diceRolled) + Yahtzeetool.smallstraight(roll.diceRolled) + Yahtzeetool.largestraight(roll.diceRolled)+ Yahtzeetool.yahtzee(roll.diceRolled) + Yahtzeetool.chance(roll.diceRolled)
	finalscores.append(score)
	#Go back to round 1
	print('SCORE: ' + score)
else:
	print('Okay, goodbye')
	exit()

#The player plays thirteen rounds, like in the actual game.


totalscore = sum(finalscores)
print('FINAL SCORE: ' + str(totalscore))


#Unable to figure out issue with code being iterable, but otherwise it should work. It was most likely an issue with calling the array, just because
#Wtih this specific error, that would make the most sense.