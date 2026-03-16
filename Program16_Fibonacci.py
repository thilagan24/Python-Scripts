


#this is the program to generate N number of Fibonacci Series that usually starts with 0 and 1.


x=0

y=1

z=int(input("Please enter how many number of fibonacci series you want to generate: "))

print(x)

print(y)

for i in range(z):

    w=x+y

    print(w)

    x=y

    y=w
