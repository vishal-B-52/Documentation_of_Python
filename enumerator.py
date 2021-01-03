# Purpose of Enumerate function :-
"""
This function takes index and item function bot to select objects from list. It is used in for loop to shorten the length
of code.
"""
# Without Enumerate function :-

list1 = ["Vishal", "Vinay", "Vijay", "Vinayak", "Vishesh", "Vilas", "Vipaksh", "Vardan"]
# i = 1
# for item in list1:
#     if i % 2:
#         print(f"Buy this items:- {item}")
#     i += 1

"""
The above code works on following mechanism -
1. i = 1 :- Initializes the value of i to 1.
2. i % 2 :- 2 will address the loop to skip every second element after 1st element. Ex:- Vishal is 1st word so Vinay will 
            be skipped. Vijay is 1st so Vinayak will be skipped.
3. is not 0 :- formality purpose. It's presence or absence does not matters.
4. print(f"Buy this items:- {item}") :- Used f-strings in the statement to address variable values in it. After execution
                                        of loop, the updated values of the variable are redirected to the variable "item". 
5. i = i + 1 -> It will increment the loop and variable everytime so that the loop won't get stuck on only one argument. It 
                will call the loop again and again until the list ends.                                                 
"""

# use of Enumerate Function :-

for index, item in enumerate(list1):
    if index % 2 == 0:
        print(f"Buy item:-{item}")

"""
The following code acquired following mechanism -
1. for index, item in enumerate(list1) :- for loop is used to loop through the list. index is used to indicate index  
                                          positions of arguments. "item" is used as a common value to redirect variable 
                                          value of list1 that is arguments. remnant is enumerate(list1). Enumerate is 
                                          used to add counter to every object in the list. This function indirectly counts 
                                          objects as per directed by the user.
2. if index % 2 == 0 :- If loop is used to state the specific condition for printing arguments. "index % 2" will tell 
                         the 'if' loop to skip every 2nd character after printing 1st element. Ex:- In above example, 
                         "Vishal" is the 1st and "Vinay" is second so it will be skipped. After Vinay, "Vijay" will be 
                         the 1st element while "Vinayak" 2nd position hence "Vinayak" will be omitted. The latter will 
                         remain same throughout end of the list and loop as well. 
                         
                         "index % 2 == 0" will initialize the starting point. Index % 2 will work with above given mechanism 
                         but "== n" is used to set initial point of loop. You can set "== 0 or ==1 or ==2 ....== n" till
                         the third last element of your loop and index % 2 will work from there. 
                         
                         Note:- "==" -> common and important.
                                ">= & <=" -> useless and not much effective.                                           
3.  print(f"Buy item:-{item}") :- Will print items or args or objects as per filtered by given condition.
"""