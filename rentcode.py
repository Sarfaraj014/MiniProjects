#taking input by the user 
Rent=int(input("Enter your total Rent : "))
spendUnit=int(input("Total Electricity units spend : "))
unitcharge=int(input("Electriciy charge per unit : "))
personNo=int(input("Number of person to devide the amount : "))

#perform substraction,multipication and divison

electricityExpences=unitcharge*spendUnit
totalAmount=(Rent + electricityExpences)/personNo

#print the final output

print(f"Each will pay = {str(totalAmount)}")