# Author: HROD
import random

# Base class representing a dice player
class DicePlayer:
    def __init__(self, name):
        self.name = name
        self.dice = []  # List to store the rolled dice values

    # Method to roll a specified number of dice and calculate the total
    def roll_dice(self, num_dice=2):
        self.dice = [random.randint(1, 6) for _ in range(num_dice)]
        return sum(self.dice)

# Base class for cheating dice players, inherits from DicePlayer
class CheatingDicePlayer(DicePlayer):
    def cheat(self):
        pass  # This method will be overridden by subclasses

# Cheating subclass: MulliganCheater - allows taking a mulligan and re-rolling if the total is less than 9
class MulliganCheater(CheatingDicePlayer):
    def cheat(self):
        total = super().roll_dice()
        if total < 9:
            print(f"{self.name} took a mulligan and re-rolled the dice.")
            total = super().roll_dice()
        return total

# Cheating subclass: ExtraDieCheater - rolls one additional die
class ExtraDieCheater(CheatingDicePlayer):
    def cheat(self):
        total = super().roll_dice()
        extra_die = random.randint(1, 6)
        print(f"{self.name} rolled an extra die: {extra_die}")
        return total + extra_die

# Cheating subclass: WeightedDieCheater - uses a weighted die (first die cannot roll below 3)
class WeightedDieCheater(CheatingDicePlayer):
    def cheat(self):
        total = super().roll_dice()
        self.dice[0] = max(self.dice[0], 3)
        print(f"{self.name} used a weighted die.")
        return total

# Cheating subclass: SabotageCheater - sabotages the opponent's dice (opponent is another DicePlayer)
class SabotageCheater(CheatingDicePlayer):
    def cheat(self, opponent):
        total = super().roll_dice()
        for i in range(len(opponent.dice)):
            opponent.dice[i] = min(opponent.dice[i], 3)
        print(f"{self.name} sabotaged {opponent.name}'s dice.")
        return total

# Example usage:
player1 = DicePlayer("Alice")
player2 = MulliganCheater("Bob")
player3 = ExtraDieCheater("Charlie")
player4 = WeightedDieCheater("David")
player5 = DicePlayer("Eve")
player6 = SabotageCheater("Frank")

players = [player1, player2, player3, player4, player5, player6]

# Roll dice for all players and display the results
for player in players:
    total = player.roll_dice()
    print(f"{player.name} rolled: {player.dice} - Total: {total}")

# Frank, the SabotageCheater, sabotages Eve's dice
player6.cheat(player5)

# Roll dice for all players again and display the results
for player in players:
    total = player.roll_dice()
    print(f"{player.name} rolled: {player.dice} - Total: {total}")
