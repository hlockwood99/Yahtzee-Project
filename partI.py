import random

class Dice():

	def dice(self ,num):
		self.dice = []
		for i in range(num):
			self.dice.append(random.randint(1,6))
		return self.dice

	def first_roll(self, array):
		input("Press ENTER")
		roll1 = self.dice(5)
		return roll1

		for 




