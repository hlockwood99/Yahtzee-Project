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

try1 = input('Would you like to roll the dice?')
while response != 'y' and response != 'n':
	print('Try again. Please type [y] or [n]')
	answer = input('Would you like to roll a die? ')
	if response == 'y':
		roll1 = Dice()
		roll1.DiceRoll()
	elif response == 'n':
		print('Come again soon!')
		break

try2 = input('Would you like to roll the dice?')
while response != 'y' and response != 'n':
	print('Try again. Please type [y] or [n]')
	answer = input('Would you like to roll a die? ')
	if response == 'y':
		roll1 = Dice()
		roll1.DiceRoll()
	elif response == 'n':
		print('Come again soon!')
		break
