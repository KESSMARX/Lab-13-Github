import functions

<<<<<<< HEAD
# Class for storing player information
=======
# ---------------------------------------------------------------------------------------
# Player Class
>>>>>>> b51cfcf8a541b8681c8a96a540b84e9ecfa3fd66
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

<<<<<<< HEAD

class battle_of_dices:
=======
# ---------------------------------------------------------------------------------------
# Game Class
class DiceGame:
>>>>>>> b51cfcf8a541b8681c8a96a540b84e9ecfa3fd66
    def __init__(self, winning_score=3):
        self.players = []
        self.rounds = 0
        self.winning_score = winning_score
        self.gameover = False

<<<<<<< HEAD
    # Function to create a new player dict
    def add_player(self):
        name = input("Name: ")
        email = input("Email: ")
        country = input("Country: ")
        new_player = Player(name, email, country, 0, [])
        self.players.append(new_player)
        
    def round(self):
        """ Play a round of the game, rolling dice for each player and decide the winner(s) of the round. """
        self.rounds += 1
        print(f"\nRound {self.rounds}:")
        rolls = {}        # <-- Use dict for player-name mapping
        winners = []      # <-- Initialize before using

        for player in self.players:
            roll = functions.rollD6() + functions.rollD6()
            player.add_roll(roll)
            rolls[player.name] = roll
            print(f"Player {player.name} rolled: {roll}")
=======
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
>>>>>>> b51cfcf8a541b8681c8a96a540b84e9ecfa3fd66

    def play(self):
        while self.gameover is False:
            self.rounds += 1
            print(f"\n--- Round {self.rounds} ---")

<<<<<<< HEAD
        for each_player in self.players:
            if each_player.rolls[-1] == max_roll:
                each_player.add_win()
                winners.append(each_player.name)
                print(f"Player {each_player.name} won in round {self.rounds}")
        print(f"Winners of this round: {winners}")

        # Check if someone has won the game
        for each_player in self.players:
            if each_player.wins >= self.winning_score:
                print(f"\n🏆 {each_player.name} is the newest Battle of Dices Champion!")
                self.gameover = True

        if not self.gameover:
            print("🔥 This heated Battle of Dices is still going on! Who will win in the end?")


# ===============================
# MAIN EXECUTION
# ===============================

game = battle_of_dices()

# Obtain the number of players 
number_of_players = int(input("How many players? "))

# For loop to obtain the player names
for i in range(number_of_players):
    print(f"\nEnter details for player {i+1}:")
    game.add_player()

# Game loop
while not game.gameover:
    game.round()
# --------------------------------------------------------------------------------------------------
# Save the results to a file 
filename = input("Enter the filename to save the results: ")
with open(filename, "w") as file: # "w" = write mode
    # Player information
    file.write("Player information:\n")

    # Saves each player information using python automatically concatenation of adjacent string
    for each_player in game.players:
        file.write(
            f"Name: {each_player.name}\n"
            f"* E-mail: {each_player.email}\n"
            f"* Country: {each_player.country}\n"
            f"* Wins: {each_player.wins}\n"
        )

    # Round history
    for r in range(game.rounds):
        # Start with empty text for this round
        rolls_str = ""

        # Go through each player and build the string step by step
        for i, each_player in enumerate(game.players):
            rolls_str += f"{each_player.name} rolled {each_player.rolls[r]}"

            # Add a comma and space unless it is the last player
            if i < len(game.players) -1:
                rolls_str += ", "

        # Now write the full round info to the file
        file.write(f"Round {r+1}: {rolls_str}\n")

    print("\nGame over! Results saved succesfully.")
=======
            current_rolls = []
            for player in self.players:
                roll = player.roll_dice()
                current_rolls.append(roll)
                print(f"{player.name} rolled: {roll}")

            max_roll = max(current_rolls)
            if current_rolls[0] != current_rolls[1]:
                winners = [p for p in self.players if p.rolls[-1] == max_roll]

                for winner in winners:
                    winner.wins += 1
                    print(f">>> {winner.name} won round {self.rounds}!")

            elif current_rolls[0] == current_rolls[1]:
                print ("No winner this time!")

            # Check if someone reached the winning score
            for player in self.players:
                if player.wins >= self.winning_score:
                    print(f"\n🏆 {player.name} is the newest Battle of Dices Champion!")
                    self.gameover = True
                    break

            if self.gameover is False:
                print("The battle continues...")

# ---------------------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------------------
# Main Program
game = DiceGame(winning_score=3)
game.setup_players()
game.play()
game.save_results()
>>>>>>> b51cfcf8a541b8681c8a96a540b84e9ecfa3fd66
