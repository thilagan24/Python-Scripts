

#cs=Current Speed
#sl=Speed Limit

sl=80

cs=int(input("Enter the current speed value:"))


if cs<sl:
    print("You are going at a permitted speed limit")

else:

    print("You are going beyond speed limit, SLOW DOWN")
