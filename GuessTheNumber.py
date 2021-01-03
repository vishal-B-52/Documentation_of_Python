
print("Welcome to Guess The Number game. You have to guess the correct number we chosen to be hidden. "
      "You will get only 10 chances to find it. Let's start!!!")
Number = 18
Guess = 10
while 1:
    your = int(input("Enter your number here:- "))

    if your == Number:
        print("Congratulations you won the game!!!")
        print("you won with", Guess, "guesses still left!!")
        break

    elif 0 < your < 17 or 19 < your < 35:
        print("You are very much close to the hidden number!!")

    elif 35 < your < 50:
        print("You are going away, stay in mid range.")

    elif 50 < your < 100:
        print("You have gone too far. Number is not there!!")

    elif your > 100:
        print("Why are you stil alive?")
    print(f"You have {Guess - 1} guesses left\n")
    Guess = Guess - 1

    if Guess == 0:
        print("Game over")
        break

