# Guess the number :-

print("This is a 'Guess the Number Game'. You have 10 Life(s) to guess the hidden number. You have to win in 10 Life(s) "
      "else You lose!!! ")
Life = 10

while True:

    N = int(input("Enter the number:- "))
    Life -= 1
    if 0 <= N < 18:
        if Life == 0:
            print("Sorry but you have lost the game, Secret number was 18.\n")
            break
        else:
            print("You are too close to the number. Try to focus!!")
    elif N == 18:
        print("Hurray You won the game !!!")
        print("You won with", Life, "life(s) still left\n")
        break
    elif 19 <= N <= 36:
        if Life == 0:
            print("Sorry but you have lost the game, Secret number was 18.\n")
            break
        else:
            print("You are close to the number, Please concentrate!!")
    elif 37 < N <= 100:
        if Life == 0:
            print("Sorry but you have lost the game, Secret number was 18.\n")
            break
        else:
            print("You are going too far. You need to come back")
    elif N > 100:

        if Life == 0:
            print("Sorry but you have lost the game, Secret number was 18.\n")
            break
        else:
            print("Number is smaller than 100, Please Try again!!!")
    if Life == 9:
        print("You lost one life,", Life, "life(s) left\n")
    elif Life == 8:
        print("You lost another life,", Life, "life(s) left\n")
    elif 1 < Life <= 7:
        print("You lost another life again,", Life, "life(s) left\n")
    elif Life == 1:
        print("You have the last life. Best of Luck.", Life, "Life(s) left\n")




