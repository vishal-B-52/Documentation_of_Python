def getdate():
    import datetime
    return datetime.datetime.now()


def getinto():
    print("This function let's you decide whether to log or retrieve data from Client's database.")
    Clienter = input("Choose A.Log and B.Retrieve\nYour Input:-")
    if Clienter == 'A':
        getlog()
    elif Clienter == 'B':
        getretrieve()
    else:
        print("wrong input!!!")


def getlog():
    print("You can log the data into client's file here.\n")
    Client = int(input("Chose client:-1.Harry 2.Rohan 3.Hammad\nYour input:-"))
    if Client == 1:
        Options = input("You have chosen Harry's database. Type 'D' for Diet and 'E' for Exercise\n")
        if Options == 'D':
            f = open("Harry-Diet.txt", "a")
            f.write(input() + " : " + str([str(getdate())]) + "\n")
        elif Options == 'E':
            f = open("Harry-Exercise.txt", "a")
            f.write(input() + " : " + str([str(getdate())]) + "\n")
    elif Client == 2:
        Options = input("You have chosen Rohan's database. Type 'D' for Diet and 'E' for Exercise\n")
        if Options == 'D':
            f = open("Rohan-Diet.txt", "a")
            f.write(input() + " : " + str([str(getdate())]) + "\n")
        elif Options == 'E':
            f = open("Rohan-Exercise.txt", "a")
            f.write(input() + " : " + str([str(getdate())]) + "\n")
    elif Client == 3:
        Options = input("You have chosen Hammad's database. Type 'D' for Diet and 'E' for Exercise\n")
        if Options == 'D':
            f = open("Hammad-Diet.txt", "a")
            f.write(input() + " : " + str([str(getdate())]) + "\n")
        elif Options == 'E':
            f = open("Hammad-Exercise.txt", "a")
            f.write(input() + " : " + str([str(getdate())]) + "\n")


def getretrieve():
    print("You can retrieve the logged client data here\n")
    Client = int(input("Chose client:-1.Harry 2.Rohan 3.Hammad\nYour Input:-"))
    if Client == 1:
        Options = input("You have entered Harry's database. Type 'D' for Diet and 'E' for Exercise\n")
        if Options == 'D':
            f = open("Harry-Diet.txt", "rt")
            print(f.read())
        elif Options == 'E':
            f = open("Harry-Exercise.txt", "rt")
            print(f.read())
    elif Client == 2:
        Options = input("You have entered Rohan's database. Type 'D' for Diet and 'E' for Exercise\n")
        if Options == 'D':
            f = open("Rohan-Diet.txt", "rt")
            print(f.read())
        elif Options == 'E':
            f = open("Rohan-Exercise.txt", "rt")
            print(f.read())
    elif Client == 3:
        Options = input("You have entered Hammad's database. Type 'D' for Diet and 'E' for Exercise\n")
        if Options == 'D':
            f = open("Hammad-Diet.txt", "rt")
            print(f.read())
        elif Options == 'E':
            f = open("Hammad-Exercise.txt", "rt")
            print(f.read())


getinto()

while 1:
    rerun = input("Do you want to try again, [y/n]?\n")
    if rerun == 'y':
        getinto()
    elif rerun == 'n':
        break