import copy
import functions

# Variables to keep track of the score
rounds = 0
gameover = False

# Nummber of wins needed to win the game
winning_score = 3

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
       

# List to store the dicts for each player
players = []

# Obtain the number of players 
number_of_players = int(input("How many players?"))

# For loop to obtain the player names
for i in range(number_of_players):

    # create a new object
    new_player = Player(input("Name: "), input("Email: "),input("Country: "), 0, [])

# Repeats until the game is over. As many rounds as necessary
while gameover is False:

    print(f"Round {rounds+1}:")
    # input ("\n Enter to continue...")

    # Dice roll for each player in the current round
    current_rolls = []

    # We need to roll the dice for each player
    for each_player in players:
        roll = functions.rollD6() + functions.rollD6()

        # player_rolls_history[i].append(roll)
        each_player["rolls"].append(roll)

        current_rolls.append(roll)

        print(f"Player {each_player['name']} rolled: {roll}")

    # Still in gameover is False

    # Obtain the highest roll this round
    max_roll = max(current_rolls)

    # Find winners of the round
    winners = []

    # Search for all players who got the highest roll
    for each_player in players:
        if (each_player["rolls"][-1] == max_roll):
            each_player["wins"] += 1
            print(f"Player {each_player['name']} won in round {rounds+1}")

            winners.append(each_player['name'])
    print(f"Winners of this round: {winners}")

    # still in the gameover False

    for each_player in players:
        if (each_player['wins'] >= winning_score):
            print(f"\n{each_player['name']} is the newest Battle of Dices Champion!")
            gameover = True
    
    if gameover is False:
        print("This heated Battle of Dices is still going on! Who will win in the end?")

    rounds += 1


# --------------------------------------------------------------------------------------------------
# Save the results to a file 
filename = input("Enter the filename to save the results: ")
with open(filename, "w") as file: # "w" = write mode
    # Player information
    file.write("Player information:\n")

    # Saves each player information using python automatically concatenation of adjacent string
    for each_player in players:
        file.write(
            f"Name: {each_player['name']}\n"
            f"* E-mail: {each_player['email']}\n"
            f"* Country: {each_player['country']}\n"
            f"* Wins: {each_player['wins']}\n"
        )

    # Round history
    for r in range(rounds):
        # Start with empty text for this round
        rolls_str = ""

        # Go through each player and build the string step by step
        for i, each_player in enumerate(players):
            rolls_str += f"{each_player['name']} rolled {each_player['rolls'][r]}"

            # Add a comma and space unless it is the last player
            if i < len(players) -1:
                rolls_str += ", "

        # Now write the full round info to the file
        file.write(f"Round {r+1}:\n {rolls_str}\n")

    print("\nGame over! Results saved succesfully.")