"""

WORKFLOW OF PROJECT:
1- Input from user (Rock, paper, scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result print
昭
Cases:
A
A- Rock
Rock - Rock =tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor

C- Scissor
Scissor - Scissor = tie
Scissor -  Rock = Rock win
Scissor - Paper = Scissor win

"""

import random 
item_list = ["Rock","Paper","Scissor"]
user_choice = input("Enter your move = Rock,Paper,Scissor= ")
comp_choice = random.choice(item_list)
print(r"User choice = {user_choice},computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: Matches tie")
elif user_choice == "Rock":
    if comp_choice == "paper":
        print("Paper cover Rock = Computer")
    else:
        print("Rock smashes scissor = You Win ")  

elif user_choice =="Paper":
    if comp_choice == "scissor":
        print("scissor cut the paper, computer win")
    else:
        print("paper cover rock , You win")
elif user_choice == "Scissor":
    if comp_choice == "Paper":
        Print("scissor cut the paper , You Win")   
    else:
        print("Rock smashes scissor = computer Win ")               