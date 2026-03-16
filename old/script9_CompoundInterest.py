

#Calculation using concept of Compound Interest

#Concept is - lender and borrower agree for a period over which is the remaining amount becomes principal after that and so on.

x=int(input("Please enter the principal amount:"))

y=int(input("Please enter the interest percentage:"))

z=int(input("Please enter the tenure in years:"))

c=int(input("OPTIONS:\n1.Annually \n2.Half-yearly \n4.Quarterly\nPlease enter how you want to compound it: "))

a=y/c

b=z*c

w=x*(1+(a/100))**b 

print("Amount you pay extra is",w)
