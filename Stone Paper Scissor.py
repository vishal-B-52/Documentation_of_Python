
import names
import random

while 1:
    opponent = names.get_full_name()
    sep_names = opponent.split(' ')
    fname = sep_names[0]
    get_name = input("\nEnter your name here: ")
    print(f"Welcome {get_name}, You are welcomed to the contest of Stone-Paper-Scissor.")
    print(f"We will be arranging your match with {opponent}.")
    sel_rounds = int(input(f"Enter the number of rounds you want to play with {opponent}: "))
    round_no = 0
    my_points = 0
    opp_points = 0
    choice = ['Stone', 'Paper', 'Scissors']
    while sel_rounds > 0:
        round_no += 1
        opp_choice = random.choice(choice)
        print("\nRound No: ", round_no)
        you_choice = input("Enter your choice[1/2/3]: ")
        if you_choice == '1':
            you_choice = 'Stone'
        elif you_choice == '2':
            you_choice = 'Paper'
        elif you_choice == '3':
            you_choice = 'Scissors'
        print(f"{get_name} selected {you_choice} vs {fname} selected {opp_choice}")
        if (you_choice == 'Stone' and opp_choice == 'Stone') or (you_choice == 'Paper' and opp_choice == 'Paper') or \
                (you_choice == 'Scissors' and opp_choice == 'Scissors'):
            print(f"Round is drawn.")
        elif (you_choice == 'Stone' and opp_choice == 'Scissors') or (you_choice == 'Paper' and opp_choice == 'Stone') or (
                you_choice == 'Scissors' and opp_choice == 'Paper'):
            print(f"{get_name} Won this round.")
            my_points += 1
        elif (you_choice == 'Stone' and opp_choice == 'Paper') or (you_choice == 'Paper' and opp_choice == 'Scissors') or (
                you_choice == 'Scissors' and opp_choice == 'Stone'):
            print(f"{fname} Won this round.")
            opp_points += 1

        print(f"\nScoreboard ---> {get_name}: {my_points} points  Vs  {fname}: {opp_points} points\n")
        sel_rounds = sel_rounds - 1

    print(f"\nFinal Scoreboard ---> {get_name} : {my_points} points  Vs  {opponent} : {opp_points} points")
    if my_points == opp_points:
        print(f"\nThe Match is drawn. {get_name} and {opponent} are equally winners.")
    else:
        if my_points > opp_points:
            print(f"\nThe winner is {get_name}.")
        elif my_points < opp_points:
            print(f"\nThe winner is {opponent}.")
    retry = input("\nDo you want to play the game again?")
    if retry == '1':
        print("Enjoy the game!!")
    elif retry == '0':
        print("Have a nice day!!")
        break
