#THis is a program to list the years between the given range


x=int(input("Please enter the start year: "))


y=int(input("Please enter the end year: "))

z=y+1


for i in range(x,z):

    if i%4==0 and i%100!=0 or i%400==0:

        print("This given year",i,"is a leap year.")

    
