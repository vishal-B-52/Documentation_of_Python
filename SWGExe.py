# This is a Snake-Water-Gun game which is written by Vishal Bawane.

Name = input("Enter your name:-")
print(f"Welcome {Name} to the Snake-Water-Gun game.\n")


def SWGExE():
    import random
    Rounds = 10
    YouW = 0
    PCW = 0
    while 1:
        PClister = ["Snake", "Water", "Gun"]
        PC = random.choice(PClister)
        You = input("Choose from following:-\n1.Snake 2.Water 3.Gun\nPlease type S, W, G instead of complete name.\nYour input:-")
        print("PC's input:-", PC)
        if You == "S" and PC == "Snake" or You == "W" and PC == "Water" or You == "G" and PC == "Gun":
            Collect = 1
        elif You == "S" and PC == "Water" or You == "W" and PC == "Gun" or You == "G" and PC == "Snake":
            Collect = 2
        elif You == "S" and PC == "Gun" or You == "W" and PC == "Snake" or You == "G" and PC == "Water":
            Collect = 3

        if Collect == 1:
            print(f"This round has been drawn. Scores = {Name} - {YouW} <||> PC - {PCW}.")
            YouW += 0
            PCW += 0

        elif Collect == 2:
            YouW += 1
            print(f"You won this round. Scores = {Name} - {YouW} <||> PC - {PCW}.")

        elif Collect == 3:
            PCW += 1
            print(f"PC won this round. Scores = {Name} - {YouW} <||> PC - {PCW}.")

        Rounds -= 1
        print(f"Rounds remaining are {Rounds}\n")

        if Rounds == 0:
            print("Game over!!!")
            print("Results :-")
            print(f"Final Score = {Name} - {YouW} <||> PC - {PCW}")
            if YouW > PCW:
                print(f"Congrats, {Name} you are winner!! You have beaten PC with {YouW - PCW} point(s).")
            elif PCW > YouW:
                print(f"You lose, PC have beaten you with {PCW - YouW} point(s)")
            elif YouW == PCW:
                print("The series is drawn. You and PC have equal point(s).")
            break



