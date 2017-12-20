# Yahtzee

###### Rules
The objective of the game is to score points by rolling five dice to make certain combinations. The dice can be rolled up to three times in a turn to try to make various scoring combinations. A game consists of thirteen rounds. After each round the player chooses which scoring category is to be used for that round. Once a category has been used in the game, it cannot be used again. The scoring categories have varying point values, some of which are fixed values and others where the score depends on the value of the dice. A Yahtzee is five-of-a-kind and scores 50 points; the highest of any category. The winner is the player who scores the most points.

![Yahtzee!](https://casualgamerevolution.com/sites/default/files/images/games/5_dice.jpg)

### Plan

There is a Dice class as well as a Yahtzee class. The Dice class will generate the numbers for each die and will provide the final values to be used for scoring. The Yahtzee class contains the conditions of Yahtzee, such as three of a kind, four of a kind, small straight, large straight, Yahtzee, etc.

Henry will be working on the Dice class and Michael will be working on the Yahtzee class.

Lastly, there will be a runner file where the user will be able to play the Yahtzee game and will be asked questions such as, "Would you like to roll again?" or "What die(s) would you like to keep?" The two will collaborate together to make this class.

### Classes

* __Dice Class__
	* init class, which gives the player the starting values for the first dice roll. This information is given in an array, and is then manipulated within the array for the rest of the code.
	* Includes DiceRoll function, takes the array from the init and then askes whether the user wants to reroll. Regardless of the answer, the user will be asked twice, just to be sure. The class ends by returning a final dice array, which holds the values which will be scored.

* __Yahtzee Class__
	* singledigits class, which adds up the single digits of the list (such as 2 3's, 2 4's, etc.)
	* threeofakind class, which adds up all of the digits of the list if there is 3 or more of a certain value
	* fourofakind class, which adds up all of the digits of the list if there is 4 or more of a certain value
	* fullhouse class, which adds up all of the digits of the list if there is 3 of the same value, and 2 of a different value
	* smallstraight class, which gives a score of 30 as long as there are 4 consecutive numbers
	* largestraight class, which gives a score of 40 as long as there are 5 consecutive numbers
	* yahtzee class, which gives a score of 50 if all of the dice have the same number
	* chance class, which adds up the total of all 5 die.

* __Runner Class__
	* The runner class asks the user whether or not he or she would like to play Yahtzee. It will ask if the player would like to roll the die, and then he or she would be given a final score for the round.

