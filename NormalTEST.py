print("Price of 1kg Rice is 16.75.")
print("Price of 1kg Sugar is 15.\n")


Rice_Quantity = float(input("Enter quantity of rice: "))
Sugar_Quantity = float(input("Enter quantity of Sugar: "))
Price_of_Rice = Rice_Quantity * 16.75
Price_of_Sugar = Sugar_Quantity * 15
Total_Bill = Price_of_Rice + Price_of_Sugar

print("\n  Item    price   Quantity   Total")
print("  ---------------------------------------")
print("  Rice    16.75\t\t", Rice_Quantity, "\t ", Price_of_Rice)
print("  Sugar   15.00\t\t", Sugar_Quantity, "\t ", Price_of_Sugar)
print(" \n  Total Bill = Rs.", Total_Bill)

