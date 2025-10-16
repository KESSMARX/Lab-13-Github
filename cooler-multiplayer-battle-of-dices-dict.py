import copy
import functions

# Class for storing player information
class Player:
    
    def __init__(self, name, email, country, wins, rolls):
        self.name = name
        self.email = email
        self.country = country
        self.wins = wins
        self.rolls = rolls

    def add_roll(self, roll):
        self.rolls.append(roll)
        
    def add_win(self):
        self.wins += 1
        
    def __str__(self):
        return f"{self.name}, ({self.country}) - Wins: {self.wins}"


class battle_of_dices:
    def __init__(self, winning_score=3):
        self.winning_score = winning_score
        self.players = []
        self.rounds = 0
        self.gameover = False

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

        max_roll = max(rolls.values())

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