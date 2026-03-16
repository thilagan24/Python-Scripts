

#this is the program to print table of your choice between 1-20


x=int(input("Please enter the number (1-20) to print Table: "))

if x<=20:    

    for i in range (1,11):

        print(x,"*",i,"=",x*i)

else:

    print("Out of range. Enter between 1-20")

    
