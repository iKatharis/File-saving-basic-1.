import random
import _random
import json

def load_save():
    try:
        with open('rps_save.json', 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return {"player_choices": [], "computer_choices": [], "score": [0, 0, 0]}

def save_game():
    data = {
        "player_choices": rps,
        "computer_choices": rpscomp,
        "score": [won, lost, tied]
    }
    with open('rps_save.json', 'w') as f:
        json.dump(data, f, indent=4)




cont = "y"
won = 0
lost = 0
tied = 0
rpschoice = ['rock', 'paper', 'scissors']
rps = []
rpscomp = []





def rpsc(player_choice):
        if player_choice not in rpschoice:
            return "Invalid choice! Please choose 'rock', 'paper', or 'scissors'."
        elif player_choice == 'rock' or 'r':
            rps.append('rock')
        elif player_choice == 'paper' or 'p':
            rps.append('paper')
        elif player_choice == 'scissors' or 's':
            rps.append('scissors')
def computer_choice():
    return random.choice(rpschoice)
def determine_winner(player, computer):
    global won, lost, tied
    if player == computer:
        tied += 1
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
        (player == 'paper' and computer == 'rock') or \
        (player == 'scissors' and computer == 'paper'):
        won += 1
        return "You win!"
    else:
        lost += 1
        return "Computer wins!"


loaded_data = load_save()
if loaded_data["player_choices"]:
    rps = loaded_data["player_choices"]
    rpscomp = loaded_data["computer_choices"]
    won, lost, tied = loaded_data["score"]
    print(f"Loaded previous game: {won}W {lost}L {tied}T")

print ("Welcome to Rock, Paper, Scissors!")
print ("___________")

while cont == "y":
    rpsc(input("rock, paper, scissors: "))
    print ("___________")

    rpscomp.append(computer_choice())
    print ("computer chose," ,rpscomp)

    print(f"Computer chose: {rpscomp[-1]}")
    print ("___________")
    print (rps, rpscomp)
    result = determine_winner(rps[-1], rpscomp[-1])
    print(result)
    print ("___________")
    rps = []
    rpscomp = []
    print(f"Score: {won} Wins, {lost} Losses, {tied} Ties")
    print(f"Current win loss ratio = {((tied * 50)+(won * 100))/(won + lost + tied)}%")
    save_game()
    print ("__________________________________________________________________________________")
    cont = input(str("Continue? (y/n)"))
    print ("__________________________________________________________________________________")