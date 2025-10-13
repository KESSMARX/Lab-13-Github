from dice import rollD6, rollD8
import copy

print("🎲 Welcome to Battle of Dices! 🎲")

rounds = 0
gameover = False
winning_score = 3

#Dictionary Template for storing player information:
player_info = {"name": "", "email": "", "country": "", "wins": 0, "rolls": []}

#List to store the dicts for each player:
players = []

number_of_players = int(input("How many players?: "))

for i in range(number_of_players):
    player = copy.deepcopy(player_info)
    
    player["name"] = input(f"What is the name of Player {i+1}?")
    player["email"] = input(f"What is the email of Player {i+1}?")
    player["country"] = input(f"Which country is Player {i+1} from?")
    
    players.append(player)

# Repeats until the game is over. As many rounds as necesarry:
while gameover is False:
    print(f"Round {rounds+1}:")
    
    # Dice roll for each player in the current round:
    current_rolls = []
    
    # We need to roll the dice for each player:
    for each_player in players:
        d6 = rollD6()
        d8 = rollD8()
        total = d6 + d8
        
        each_player["rolls"].append(total)
        current_rolls.append(total)
        print(f"Player {each_player["name"]} rolled a D6={d6} D8={d8} (Total={total}): ") 
               
#... still in the while gameover is False:

#Obtain the highest roll this round:
    max_roll = max(current_rolls)
#Winners will store information about who won this round:
    winners = []
#Search for all players who got the highest roll:
    for each_player in players:
        if(each_player["rolls"][-1] == max_roll):
            each_player["wins"] += 1
            print(f"Player {each_player['name']} won in round {rounds+1}")
            
            winners.append(each_player['name'])
    print(f"Winners of this round are: {winners}")   
    
    for each_player in players:
        if(each_player["wins"] >= winning_score):
            print(f"\n{each_player['name']} is the newest Battle of Dices Champion! ")
            gameover = True
    
    if gameover is False:
        print("This heated Battle of Dices is still going on! Who will win in the end? ")
    
    rounds += 1
         
# Save results to a file
filename = input("Enter the filename to save the results: ")
with open(filename, "w") as file:
    # Player information:
    file.write("Player Information:\n")
    
    for each_player in players:
        file.write(
        f"Name: {each_player['name']}\n"
        f"* E-mail: {each_player['email']}\n"
        f"* Country: {each_player['country']}\n"
        f"* Wins: {each_player['wins']}\n\n")
    file.write("\nGame rounds:\n")
        
    for r in range(rounds):
        rolls_str = ""
        
        for i, each_player in enumerate(players):
            rolls_str += f"{each_player['name']} rolled {each_player['rolls'][r]}"
            
            if i < len(players) - 1:
                rolls_str += ", "
                
        file.write(f"Round {r+1}:\n {rolls_str}\n")
     
    print("\nGame over! Results saved succesfully.")