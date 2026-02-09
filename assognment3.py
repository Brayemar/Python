# In this Assignment you will come Up with a Program that will store someGross Salary in variable, Then Using If Else...Else if Statements Determine the Monthly Contribution Someone will Pay.

Gross_income = int(input("Enter the gross income: "))
if Gross_income > 0 and Gross_income < 5999:
    print("The monthly contribution is Ksh.150.00")
elif Gross_income >= 6000 and Gross_income <= 7999:
    print("The monthly contribution is Ksh.300.00") 
elif Gross_income >= 8000 and Gross_income <= 11999:
    print("The monthly contribution is Ksh.400.00") 
elif Gross_income >= 12000 and Gross_income <= 14999:
    print("The monthly contribution is Ksh.500.00") 
elif Gross_income >= 15000 and Gross_income <= 19999:
    print("The monthly contribution is Ksh.600.00") 
elif Gross_income >= 20000 and Gross_income <= 24999:
    print("The monthly contribution is Ksh.750.00") 
elif Gross_income >= 25000 and Gross_income <= 29999:
    print("The monthly contribution is Ksh.850.00") 
elif Gross_income >= 30000 and Gross_income <= 49999:
    print("The monthly contribution is Ksh.1000.00") 
elif Gross_income >= 50000 and Gross_income <= 99999:
    print("The monthly contribution is Ksh.1500.00")
elif Gross_income > 100000:
    print("The monthly contribution is Ksh.2000.00")
else:
    print("Not Qualified")