from Dice import dice
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

	