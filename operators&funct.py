# Different Operators and examples.

# A. Arithmatic Operators - Used for mathematical purpose.
"""

'+'= Addition purpose.
'-' = Subtraction Purpose.
'*' = Multiplication purpose.
'/' = Division purpose.
'//' = Divides and displays round figured value. For.ex;- Result= 2.3 then it will show 2 as answer.
'**' = displays square of the number.
'%' = returns remainder of division(modulus).

"""

# B. Assignment operator - directly assigns and operates value.
"""

'=' = Assigns value to the variable. ex. X = 5.
'+=' = adds the assigned value to the variable directly. Ex;- X += 5.
'-=' = subtracts the assigned value from variable. 
'*=' = Multiplies the assigned value to the variable.
'/=' = Divides the assigned value to variable.
'**=' = exponentiates as per the assigned number.
'//=' = divides assigned value with given number and presents round figured answer. 
'%=' = returns modulus of the division.

"""

# C. Comparison operator - compares two variables.
"""

'==' = equal to
'!=' = not equal to
'>' = greater than
'<' = less than
'>' = greater than equal to
'<' = less than equal to

"""

# D.Logical Operator - They return boolean values depending on conditions of the operators.

"""

'AND' - returns True if both variable are TRUE. Returns false if any variable returns false value.
'OR' - Returns True value if any one of two variable is True, if not then returns false.
'NOT' - Returns reverted value of the final answer. (True> False and False > TRue)

"""

# E. Identity Operators - Compares values.
"""

'is' = Returns true if a two variable are same .
'is not' = Returns True if both variables are not same. 

"""

# F. Membership operators
"""

'in' = Returns true if the element is present at the place.
'not in' = Returns true if the element is not present at the place.

"""

# G.Bitwise operator - Works on bits. That is 1 or 0. They use bit values for a number's explaination.

"""

& - And operator.
| - OR operator.
~ - Not operator
^ - XOR operator

0 - 00
1 - 01
2 - 10
3 - 11

1. And operators 
"""
# print(50 & 21)

"""
Here, AND is the operator and both numbers are '2'.

2 -   10 | 2 is displayed as '10' in bits.
       & 
1 -   01 | 1 is displayed as '01' in bits.
     ----| In Bitwise AND operation, '1-1' is '1' - '0-0'is '0' and '1-0' or '0-1' is '0'
      10 | After calculation it presents result.

Not only single digit but two digits can be anded together. Like print(50 & 21) or (75 & 22). In such cases,

50 -   110010 | when two digits are there, use the '2^' method and do the and in single set(do not divide it in two sets)
         & 
21 -   010101 |
       -------|                
       010000 | i.e. 16 will be the answer. The same procedure repeats in case of second example.
       
"""
# Bitwise OR :-

# print(23 | 34)

"""
       
In bitwise OR operation, The symbol used is '|' and '1-1' is '1' - '0-0'is '0' and '1-0' or '0-1' is '1'. 
as we have seen single digit and, we will try to or two digit numbers.
The formula and steps will be same in OR as they were in AND. The operation will just follow it's own rules to 'OR' the 
two numbers which is explained in the first line.

Here, the result will be 55.
"""

# Bitwise NOT -

# print(~34)

"""

    
In bitwise NOT operation, The symbol used is '~' which means negation. After using it on a number, a negative sign and 
                          additional "1" is added to the normal bit value.
                          
In above example, after statement is executed,

~67 = -67
    = -(1000011)
    = -(1000011 + 1)
    = -(1000011)
    = -68
    
Here, In NOT operations, the bit value of a number doesn't changes except it's sign and addition of '+1' into previous value.
For EX:- If the value was 45, then modified value will be '-46'. If value is 55, then modified value will be '-56' and it 
         goes on. 
              
"""

# Bitwise XOR operator :-

# print(23 ^ 33)

"""
In Bitwise XOR operator, '^' symbol is used to denote XOR. 
The bit values turns to '1' if alternate pair is '1-0' or '0-1' else the bit value will be '0'.
In above example, the operation will be like ,

23 -   010111 | 23 decoded into bit value.
         ^
33 -   100001 | 33 decoded.........
       ------
       110110 | The result is 54. As you can see, the pairs of '1-1' and '0-0' were resulted into '0' while alternate 
                pairs resulted into true. Except the operation, Other things are as same as they wre in OR and AND operations.
                
"""
