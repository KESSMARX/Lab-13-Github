# Lab-13-Github
Creating the ulitmate Battle of Dices together with the team 'The Jazzers'!


Hey Hey,

I just set up a code. Feel free to check and to try it out. 






import functions

# ---------------------------------------------------------------------------------------
# Player Class
class Player:
    def __init__(self, name, email, country):
        self.name = name
        self.email = email
        self.country = country
        self.wins = 0
        self.rolls = []

    def roll_dice(self):
        """Roll 2 D6 dice, save the result, and return it."""
        roll = functions.rollD6() + functions.rollD6()
        self.rolls.append(roll)
        return roll

    def __str__(self):
        return f"{self.name} ({self.country}) - Wins: {self.wins}"


# ---------------------------------------------------------------------------------------
# Game Class
class DiceGame:
    def __init__(self, winning_score=3):
        self.players = []
        self.rounds = 0
        self.winning_score = winning_score
        self.gameover = False

    def setup_players(self):
        try:
            number_of_players = int(input("How many players? "))
            for i in range(number_of_players):
                name = input(f"What is the name of Player {i+1}? ")
                email = input(f"What is the e-mail of Player {i+1}? ")
                country = input(f"What is the country of Player {i+1}? ")
                player = Player(name, email, country)
                self.players.append(player)
        except:
            print ("ERROR! - Please type in a valid number - ERROR!")

    def play(self):
        while self.gameover is False:
            self.rounds += 1
            print(f"\n--- Round {self.rounds} ---")

            current_rolls = []
            for player in self.players:
                roll = player.roll_dice()
                current_rolls.append(roll)
                print(f"{player.name} rolled: {roll}")

            max_roll = max(current_rolls)
            winners = [p for p in self.players if p.rolls[-1] == max_roll]

            for winner in winners:
                winner.wins += 1
                print(f">>> {winner.name} won round {self.rounds}!")

            # Check if someone reached the winning score
            for player in self.players:
                if player.wins >= self.winning_score:
                    print(f"\n🏆 {player.name} is the newest Battle of Dices Champion!")
                    self.gameover = True
                    break

            if self.gameover is False:
                print("The battle continues...")

# ---------------------------------------------------------------------------------------
'''
    def save_results(self):
        filename = input("\nEnter the filename to save the results: ")
        with open(filename, "w") as file:
            file.write("Player information:\n")
            for p in self.players:
                file.write(
                    f"Name: {p.name}\n"
                    f"* E-mail: {p.email}\n"
                    f"* Country: {p.country}\n"
                    f"* Wins: {p.wins}\n"
                )

            file.write("\nRound history:\n")
            for r in range(self.rounds):
                rolls_str = ", ".join(
                    f"{p.name} rolled {p.rolls[r]}" for p in self.players
                )
                file.write(f"Round {r+1}: {rolls_str}\n")

        print(f"\nGame over! Results saved successfully in '{filename}'.")
'''

# ---------------------------------------------------------------------------------------
# Main Program
game = DiceGame(winning_score=3)
game.setup_players()
game.play()
#   game.save_results()
