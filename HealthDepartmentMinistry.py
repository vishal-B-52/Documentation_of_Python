
def TimetoTime():
    import datetime
    return datetime.datetime.now()


def Client_LogOn():
    print("Welcome to Health Department Ministry. We can provide records of our clients.\n")
    LogON = int(input("Choose whether you want to read or Log data. 1.Log and 2.Read\n"))
    if LogON == 1:
        print(Client_log())
    elif LogON == 2:
        print(Client_Receiver())


def Client_log():
    print("You can enter data here. Choose which client's profile you want to modify:- ")
    Logger = int(input("1.Harry   2.Vishal   3.Peter\n"))
    if Logger == 1:
        print("You are now in Harry's database.")
        Harry_D = int(input("Choose 1.Diet/t2.Exercise\n"))
        if Harry_D == 1:
            with open("Harry_Diet.txt", "a") as A:
                return A.write(input() + " : " + str([str(TimetoTime())]) + "\n")
        elif Harry_D == 2:
            with open("Harry_Exercise.txt", "a") as B:
                return B.write(input() + " : " + str([str(TimetoTime())]) + "\n")
    if Logger == 2:
        print("You are now in Vishal's database.")
        Vishal_D = int(input("Choose 1.Diet/t2.Exercise\n"))
        if Vishal_D == 1:
            with open("Vishal_Diet.txt", "a") as C:
                return C.write(input() + " : " + str([str(TimetoTime())]) + "\n")
        elif Vishal_D == 2:
            with open("Vishal_Exercise.txt", "a") as D:
                return D.write(input() + " : " + str([str(TimetoTime())]) + "\n")
    if Logger == 3:
        Peter_D = int(input("Choose 1.Diet/t2.Exercise\n"))
        if Peter_D == 1:
            with open("Peter_Diet.txt", "a") as E:
                return E.write(input() + " : " + str([str(TimetoTime())]) + "\n")
        elif Peter_D == 2:
            with open("Peter_Exercise.txt", "a") as F:
                return F.write(input() + " : " + str([str(TimetoTime())]) + "\n")


def Client_Receiver():
    print("You can get any type of information from here.")
    Receiver = int(input("Choose a client:- 1.Harry  2.Vishal  3.Peter\n"))
    if Receiver == 1:
        print("You have entered into Harry's database.")
        Harry_D2 = int(input("Choose from:- 1.Diet   2.Exercise\n"))
        if Harry_D2 == 1:
            with open("Harry_Diet.txt", "rt") as G:
                return "The data is:-\r" + G.read()
        elif Harry_D2 == 2:
            with open("Harry_Exercise.txt", "rt") as H:
                return "The data is:-\r" + H.read()
    if Receiver == 2:
        print("You have entered into Vishal's database.")
        Vishal_D2 = int(input("Choose from:- 1.Diet   2.Exercise\n"))
        if Vishal_D2 == 1:
            with open("Vishal_Diet.txt", "rt") as I:
                return "The data is:-\r" + I.read()
        elif Vishal_D2 == 2:
            with open("Vishal_Exercise.txt", "rt") as J:
                return "The data is:-\r" + J.read()
    if Receiver == 3:
        print("You have entered into Peter's database.")
        Peter_D2 = int(input("Choose from:- 1.Diet   2.Exercise\n"))
        if Peter_D2 == 1:
            with open("Peter_Diet.txt", "rt") as K:
                return "The data is:-\r" + K.read()
        elif Peter_D2 == 2:
            with open("Peter_Exercise.txt", "rt") as L:
                return "The data is:-\r" + L.read()


Client_LogOn()

