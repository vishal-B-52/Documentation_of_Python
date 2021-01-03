import random
import names


def ROPASE():
    opponent = names.get_full_name()
    taker = input("You are welcomed to the contest, Player. May I know your name:- \n")
    print(
        f'{taker}, You are welcome as a new opponent in this RPS contest.\nYou have to play Rock-Paper-Scissor with {opponent}'
        f" to get the winner's title.\nYou will get only 10 rounds to play on and You should beat {opponent}.")
    Rounds = 0
    Youw = 0
    PCW = 0
    while True:
        List = ["Rock", "Paper", "Scissor"]
        You = input("Select any one of the following:-\r 1. Rock  2. Paper  3. Scissor\n")
        PC = random.choice(List)
        if You == 'R' and PC == 'Scissor' or You == '2' and PC == 'Rock' or You == '3' and PC == 'Paper':
            print(f"{taker} won the round.")
            Youw += 1
        elif You == '3' and PC == 'Rock' or You == '1' and PC == 'Paper' or You == '2' and PC == 'Scissor':
            print(f"{opponent} won the round.")
            PCW += 1
        elif You == '1' and PC == 'Rock' or You == '2' and PC == 'Paper' or You == '3' and PC == 'Scissor':
            print(f"The round has been drawn.")
            Youw += 0
            PCW += 0
        Rounds += 1
        if Rounds == 10:
            print("\n ! !Game Over! !")
            print("The scores are being calculated and ........\n")
            if Youw > PCW:
                print(taker + "won the game with " + Youw + " wins!!!")
                print(f"The final scores are : {taker}[{Youw}]-{opponent}[{PCW}]")
                break
            elif PCW > Youw:
                print(f"{opponent} has won the game with {PCW} wins")
                print(f"The final scores are : {opponent}[{PCW}]-{taker}[{Youw}]")
                break
            elif Youw == PCW:
                print("Both players are winner !!!!!!!!")
                print(f"The final scores are : {opponent}[{PCW}]-{taker}[{Youw}]")
                break
        print(f"The Overall score is  {Youw}-{PCW}.{10 - Rounds}rounds are still remaining.\n")


ROPASE()

Reruneer = input("Do you want to play the game again?[Y/N]")
if Reruneer == 'Y':
    print(ROPASE())
else:
    import sys
    print(sys.exit())