#Yahtzee Game Functions
import random
class Dice:
	def __init__(self):
		self.diceRolled = []
		for i in range(0,5):
			self.diceRolled.append(int(random.randrange(1,7)))

			#This part makes the first roll for the player and is the array which the code manipulates later on.

	def DiceRoll(self):
		# It was difficult to try and use condensed code to write this part, so the if statements walk the player through rerolling the dice.
		# It may look messy, but I had a lot of trouble trying to get the condensed version to work. 
		print(self.diceRolled)
		firstHold = input('Would you like to reroll any of these dice? y/n ')
		if firstHold == 'y':
			diceHold1 = input('Would you like to reroll the first die, '+str(self.diceRolled[0])+'? (y/n) ')
			if diceHold1 == 'y':
				self.diceRolled[0] = int(random.randrange(1,7))
				print(self.diceRolled)
			else:
				print('Holding')
			diceHold2 = input('Would you like to reroll the second die, '+str(self.diceRolled[1])+'? (y/n) ')
			if diceHold2 == 'y':
				self.diceRolled[1] = int(random.randrange(1,7))
				print(self.diceRolled)
			else:
				print('Holding')
			diceHold3 = input('Would you like to reroll the third die, '+str(self.diceRolled[2])+'? (y/n) ')
			if diceHold3 == 'y':
				self.diceRolled[2] = int(random.randrange(1,7))
				print(self.diceRolled)
			else:
				print('Holding')
			diceHold4 = input('Would you like to reroll the fourth die, '+str(self.diceRolled[3])+'? (y/n) ')
			if diceHold4 == 'y':
				self.diceRolled[3] = int(random.randrange(1,7))
				print(self.diceRolled)
			else:
				print('Holding')
			diceHold5 = input('Would you like to reroll the fifth die, '+str(self.diceRolled[4])+'? (y/n) ')
			if diceHold5 == 'y':
				self.diceRolled[4] = int(random.randrange(1,7))
				print(self.diceRolled)
			else:
				print('Holding')

		# After each statement, the player either choses "Reroll", in which case, a new random number between 1 and 6 will be generated.
		# The other option the player has is to "Hold" and the player is able to hold a dice for one reroll, but then reroll it the next
		else:
			print("Okay, these are the die you have: "+str(self.diceRolled))
		print('These are the dice you have now '+str(self.diceRolled)+'.') 

		secHold = input("Would you like to reroll any of these dice? (y/n) ")
		if secHold == 'y':
			dice2Hold1 = input('Would you like to reroll the first die, '+str(self.diceRolled[0])+'? (y/n) ')
			if dice2Hold1 == 'y':
				self.diceRolled[0] = int(random.randrange(1,7))
				print(self.diceRolled)
			else:
				print('Holding')
			dice2Hold2 = input('Would you like to reroll the second die, '+str(self.diceRolled[1])+'? (y/n) ')
			if dice2Hold2 == 'y':
				self.diceRolled[1] = int(random.randrange(1,7))
				print(self.diceRolled)
			else:
				print('Holding')
			dice2Hold3 = input('Would you like to reroll the third die, '+str(self.diceRolled[2])+'? (y/n) ')
			if dice2Hold3 == 'y':
				self.diceRolled[2] = int(random.randrange(1,7))
				print(self.diceRolled)
			else:
				print('Holding')
			dice2Hold4 = input('Would you like to reroll the fourth die, '+str(self.diceRolled[3])+'? (y/n) ')
			if dice2Hold4 == 'y':
				self.diceRolled[3] = int(random.randrange(1,7))
				print(self.diceRolled)
			else:
				print('Holding')
			dice2Hold5 = input('Would you like to reroll the fifth die, '+str(self.diceRolled[4])+'? (y/n) ')
			if dice2Hold5 == 'y':
				self.diceRolled[4] = int(random.randrange(1,7))
				print(self.diceRolled)
			else:
				print('Holding')
		else:
			print('Here are the dice that you will score for this round:')
			print(self.diceRolled)
# This is the end of the if statement and reroll code, and so the final array for the dice is returned by the function
		return self.diceRolled

mydie = Dice()
mydie.DiceRoll()

