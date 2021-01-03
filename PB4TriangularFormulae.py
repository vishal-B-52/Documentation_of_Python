# Area of Triangle
# Mathematical formula :- S = (a + b + c)/2

a = int(input("Enter value for a:-"))
b = int(input("Enter value for b:-"))
c = int(input("Enter value for c:-"))
#
def triangle_SemiPerimeter():
    s = (a + b + c)/2
    print(f"\nThe area of Triangle is {s}")

# Perimeter of a Triangle:-
# Mathematical Formula :-
def triangle_AreaOfTringle():
    s = s*(s-a)*(s-b)*(s-c)*0.5
    print()