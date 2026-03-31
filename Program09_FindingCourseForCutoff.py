

#this is the program that outputs the most preferred courses by students.

#Course selection must be based on passion or interest not on trend.

#Just a program to demonstrate if-else condition block

#Notice the nested if-else block eg. Inside the medicine if statement.


x=int(input("Please Enter the mark obtained in 12th:"))


if x>=90:

    print("You may choose Medicine as your course.")

    if x>=95:
        print("And you may prefer Cardio for pg in future.")

    elif x>=93:
        print("And you may prefer dematology for pg in future")

    else:
        print("And you may prefer pysiology for pg in future")

elif x>=80:

    print("You may choose Engineering as your course")

elif x>=70:

    print("You may choose commerce or Art and Science as your course")

elif x>=60:

    print("Your may choose Diploma")

else:

    print("Please choose the course based on availablity")
