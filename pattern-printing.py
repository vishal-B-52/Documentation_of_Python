# Pattern Printing -
"""
An exercise to print star pattern in half-pyramid according to the rows entered as input.
"""

print("How many rows you want?:-")
one = int(input())  # Variable 'One' will take value for rows. Means printing stars horizontally.
print("Type '1' or '0' for straight or reverted structure:-")
two = int(input())  # 'Two' variable will be used to address the code to keep the pyramid either straight or forward.
new = bool(two)  # This variable will convert entered integer value of two into boolean value like True and false.

if new == True:
    for i in range(1, one + 1):
        # This loop will decide the range of rows between 1 to specified number.
        # The range should be incremented because the range will exclude the last number from
        # range while printing. Ex;- one = 5. After printing the code, it will show only 4 rows
        # printed while last row remains unprinted. To avoid this, add 1 again to the 'One' variable and this time you
        # will obtain the same number of rows as entered. If you try to add further numbers like, One + 2 or One + 4.
        # rows will increase according to it. One + 2 wil increase one more additional row in whatever you have entered
        # for rows and One + 3 will increase 2 more rows in pyramid than the original value of 'One'.
        for j in range(i):
            # This loop decides the distribution of columns based on row's numbers. You can enter 'i' only or '1, i + 1'
            # in j's range. Don't use only 'i + 1' as it omits previous lines and increments new lines.
            # The result of 'j' with only 'i+1" will be -

            # * *
            # * * *
            # * * * *
            # * * * * *
            # * * * * * *

            # As you can see, input was '5'. Thus five lines were expected to be print here. But due to 'i+1' first line
            # was omitted and a new 6-star line was printed. Thereof, it just shifted the range for 'j'. It is useful and
            # irritating method to adjust range of iteration. Thus, Be sure to use 'i' or '1, i + 1' in 'j'. Additionally,
            # The fault was undefined range of j. only i+1 cannot assume length of '0' or '1' and hence, a programmer need
            # to define it in order to address 'j' from misprint.

            # Here, I am using 'i(variable)' only as 'j' will copy the overall range time to time rom 'i' loop.
            # range's default initial point is always '0'. You can add values in i too. Ex:- i + 2 in the range will effect
            # pyramid neutrally. here, let i's value be 7. When i is added with 2, the initial point transfers from 0 to
            # 2 directly where starting 2 rows will be ignored in printing pyramid and additional 2 rows will be added.
            # Means the rows with 1 and 2 will be ignored and 8 and 9 will add in the pyramid. It will be as follows:-

            # ***
            # ****
            # *****
            # ******
            # *******
            # ********
            # *********
            # **********

            print("*", end=" ")  # This will address the code to print the specified sign or letter in order to arrange
            # the rows and columns according to the numbers. you can use '#', '@' or anything in place of '*'. 'end = ""'
            # will keep every row in a straight line than letting it print in a vertical column. The default space is the
            # best as used in the above end= function. if you increase space between these two quotes, it will increase
            # space in stars of printed rows. It will display the structure like this-

            # *
            # * *
            # * * *
            # * * * *
            # * * * * *
            # * * * * * *

        # If you do not want to use "end=" function, remove it from the above print function and type "\r" in the lower
        # print statement. The '\r' alone is capable of arranging the stars in appropriate pyramid shape.
        print("")

    # It will print the complete structure of rows and columns embodied with '*'. Make sure to type the print()
    # function in the end of inner loop and not outer loop. If you print in inner loop, position of stars will not be
    # considered and all things will printed in a vertical line. For Ex:-

    # *
    # *
    # *
    # *
    # *
    # *
    # *
    # *
    # *
    # *
    # *
    # *
    # *
    # *
    # *

    # if you type print, outside outer loop, a horizontal line of star will occur. For Ex:-

    # * * * * * * * * * * * * * * *


elif new == False:
    for i in range(one, 0, -1):
        # this loop will decide the flow of reverted algorithm of pyramid. This condition works similar and has similar
        # argument like above if statement. The only additional things is in first loop. the first loop will decide how
        # to revert the pyramid on basis of entered number of rows. The first two things will decide the descending range
        # of pyramid. The number you have assigned to variable 'One' to 0 will be the descending range for pyramid. '-1'
        # is used here two reverse the order. In this loop, if you only type "one, 0" and vice-versa without adding -1 to
        #  the end, then it will print nothing. So, It is necessary to add '-1' in the end in first loop if you want to
        # revert the structure. You can increment variable 'one' in the loop. It will increase the final range of loop.
        # As well as, Do not mess with the second argument '0' which defines the start of pyramid from downwards. Because
        # as I said, Python does not takes the ending range as granted and considers it's previous value as the ending range.
        # FOr Ex:- taking 1 as end range will set the value as 2. '5' as end range will st the value as '6'.
        # For Ex:- for i in range(one + 2, 0, -1)
        # let one = 5
        #     type :- 0
        #     result :- *******
        #               ******
        #               *****
        #               ****
        #               ***
        #               **
        #               *
        # The additional increment of two in One resulted in increasing the final range from 5  to 7 while initial value
        # remains the same. Along with that, if you changed '-1' to '-2' then it will skip the second row respectively.
        # The outer loop will skip the number of rows you have entered in place of '-1'.
        for j in range(i):
            # This loop decides the distribution of columns based on row's numbers. You can enter 'i' only or '1, i + 1'
            # in j's range.
            # Here, I am using i only as range's default initial point is always '0'. You can add values in i too. Ex:-
            # i + 2 in the range will effect pyramid neutrally. here, let I's value be 7. When i is added with 2, the
            # initial point transfers from 0 to 2 directly where starting 2 rows will be ignored in printing pyramid and
            # additional 2 rows will be added.Means the rows with 1 and 2 will be ignored and 8 and 9 will add in the
            # pyramid. It will be as follows:-

            # ***
            # ****
            # *****
            # ******
            # *******
            # ********
            # *********
            # **********

            print("*", end=" ")
        print()
        # It will print the complete structure of rows and columns embodied wit '*'. Make sure to type the print()
        # function in the end of inner loop and not outer loop.
