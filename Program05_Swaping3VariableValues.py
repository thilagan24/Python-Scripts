#Getting values for 3 variable and swapping those values
#x should hold value of y
#y should hold value of z
#z should hold value of x


x=int(input("Enter x:"))

y=int(input("Enter y:"))

z=int(input("Enter z:"))

print("Values of x,y,z before swapping:",x,y,z)

temp=int()
temp=x
x=y
y=z
z=temp


print("Values of x,y,z after swapping:",x,y,z)

