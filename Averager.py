
print("You can check here whether an alphabet is a vowel or not.")

take_input = input("\nEnter an alphabet: ")
List_of_Vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

if take_input in List_of_Vowels:
    print(take_input + " is a vowel.")
else:
    print(take_input+" is not a vowel.")