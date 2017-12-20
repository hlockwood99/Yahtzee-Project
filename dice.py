#Yahtzee Game Functions
import random
class Dice:
	def __init__(self):
		self.diceRolled = []
		for i in range(0,5):
			self.diceRolled.append(int(random.randrange(1,6)))

	'''
		self.One = int(random.randrange(1,6))
		self.Two = int(random.randrange(1,6))
		self.Three = int(random.randrange(1,6))
		self.Four = int(random.randrange(1,6))
		self.Five = int(random.randrange(1,6))
	'''
	def DiceRoll(self):
		print(self.diceRolled)
		choice = input('What would you like to roll again? Type NONE to move on. ')
		choiceA = choice.replace(' ','').split(',')
		for i in choiceA:
			self.diceRolled[i] = random.randrange(1,6)
		print(self.diceRolled)
		return self.diceRolled
mydie = Dice()
mydie.DiceRoll()



'''
		print(diceRolled)
		choice2 = input('What would you like to roll again? Type NONE to move on. ')
		choice2 = choice2.replace(' ','').split(',')
		for i in choice2:
			diceRolled[i] = random.randrange(1,6)
'''

'''
		diceRolled.append(self.One)
		diceRolled.append(self.Two)
		diceRolled.append(self.Three)
		diceRolled.append(self.Four)
		diceRolled.append(self.Five)'''

'''
		firstHold = input('Would you like to reroll any of these dice? y/n ')
		if firstHold == 'y':
			diceHold1 = input('Would you like to reroll the first die, '+str(self.One)+'? (y/n) ')
			if diceHold1 == 'y':
				diceRolled.pop([0])
				self.One = int(random.randrange(1,6))
				diceRolled.insert(0,self.One)
			diceHold2 = input('Would you like to reroll the second die, '+str(self.Two)+'? (y/n) ')
			if diceHold2 == 'y':
				self.Two = int(random.randrange(1,6))
			diceHold3 = input('Would you like to reroll the third die, '+str(self.Three)+'? (y/n) ')
			if diceHold3 == 'y':
				self.Three = int(random.randrange(1,6))
			diceHold4 = input('Would you like to reroll the fourth die, '+str(self.Four)+'? (y/n) ')
			if diceHold4 == 'y':
				self.Four = int(random.randrange(1,6))
			diceHold5 = input('Would you like to reroll the fifth die, '+str(self.Five)+'? (y/n) ')
			if diceHold5 == 'y':
				self.Five = int(random.randrange(1,6))


		elif firstHold == 'n':
			print('Okay, now you will score the dice you have')
'''


# ⚀ ⚁ ⚂ ⚃ ⚄ ⚅

# Yahtzee
# Dice


'''




'''