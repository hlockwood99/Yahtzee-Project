#Yahtzee Game Functions
import random
class Dice:
	def __init__(self):
		self.One = int(random.randrange(1,6))
		self.Two = int(random.randrange(1,6))
		self.Three = int(random.randrange(1,6))
		self.Four = int(random.randrange(1,6))
		self.Five = int(random.randrange(1,6))
	def DiceRoll(self):
		diceRolled = []
		diceRolled.append(self.One)
		diceRolled.append(self.Two)
		diceRolled.append(self.Three)
		diceRolled.append(self.Four)
		diceRolled.append(self.Five)
		print(diceRolled)
mydie = Dice()
mydie.DiceRoll()


# ⚀ ⚁ ⚂ ⚃ ⚄ ⚅

# Yahtzee
# Dice


'''
firstHold = input('Would you like to hold any of these dice? y/n ')

if firstHold == 'y':
			diceHold1 = input('Would you like to hold the first die, '+str(self.One)+'?')
			diceHold2 = input('Would you like to hold the second die, '+str(self.Two)+'?')
			diceHold3 = input('Would you like to hold the third die, '+str(self.Three)+'?')
			diceHold4 = input('Would you like to hold the fourth die, '+str(self.Four)+'?')
			diceHold5 = input('Would you like to hold teh fifth die, '+str(self.Five)+'?')


		elif firstHold == 'n':
			print('Okay, now you will score the dice you have')

'''