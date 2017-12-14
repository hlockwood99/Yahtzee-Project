
#Yahtzee Game Functions
import random
class Dice():
	def __init__(self):
		self.diceArray = [random.randint(1,6) for _ in range(5)]
	def DiceRoll(self):
		print(self.diceArray)
Dice = Dice()
print(Dice)
# ⚀ ⚁ ⚂ ⚃ ⚄ ⚅

# Yahtzee
# Dice
