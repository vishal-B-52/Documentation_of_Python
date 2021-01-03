
print("You can check here whether a character is a vowel or not.\n")

Take_Input = input("Enter any alphabet: ")
List_of_Vowel = ['A', 'a', 'E', "e", "I", "i", "O", "o", "U", "u"]

if Take_Input in List_of_Vowel:
    print(Take_Input + " is a Vowel.")
else:
    print(Take_Input + " is not a vowel.")