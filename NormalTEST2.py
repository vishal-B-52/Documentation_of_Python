
print("The price of 1kg Rice is Rs. 16.75.")
print("The price of 1kg Sugar is Rs. 15.00.\n")

Rice_Quantity = float(input("Enter quantity of Rice: "))
Sugar_Quantity = float(input("Enter quantity of Sugar: "))
Price_Of_Rice = Rice_Quantity * 16.75
Price_Of_Sugar = Sugar_Quantity * 15.00
Total_Bill = Price_Of_Rice + Price_Of_Sugar

print("\n Item      Price      Qty      Total")
print("--------------------------------------")
print(" Rice      16.75\t  "+str(Rice_Quantity)+"\t\t"+str(Price_Of_Rice))
print(" Rice      16.75\t  "+str(Sugar_Quantity)+"\t\t"+str(Price_Of_Sugar))
print("\n  Total Bill =  "+str(Total_Bill))