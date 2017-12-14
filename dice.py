
#Yahtzee Game Functions

class Dice():
	__init__(self):
		self.One = int(random.randrange(0,7))
		self.Two = int(random.randrange(0,7))
		self.Three = int(random.randrange(0,7))
		self.Four = int(random.randrange(0,7))
		self.Five = int(random.randrange(0,7))
	def DiceRoll():
		diceArray = [self.One, self.Two, self.Three, self.Four, self.Five]


		q = str(input('Would you like to roll the dice? (y/n) ')) 
		if q == 'y':
	
			counter+=1
			DiceRolled = [One,Two,Three,Four,Five]

			print(DiceRolled)


		if q == 'n':
			print('Game Over')

		else:
			print('Well that was not one of the two letters we asked for so I guess you dont want to play')
			print('Game Over')

# ⚀ ⚁ ⚂ ⚃ ⚄ ⚅

# Yahtzee
# Dice
