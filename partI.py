import random

class Dice():

	def dice(self ,num):
		dice = []
		for i in range num:
			dice.append(random.randint(1,6))
		return dice

	def first_roll(self):
		raw_input("Press ENTER")
		roll1 = self.dice(5)
		return roll1