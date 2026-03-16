

# Creating Patterns


print(" CREATING PATTERNS \n Please Enter Desired Pattern:")

print(" 1.SQUARE \n 2.LEFT-HANDED TRIANGLE \n 3.RIGHT-HANDED TRIANGLE \n 4.TRIANGLE \n 5.HOUR-GLASS  ")

pattern=int(input())

if pattern==1:


#Square

	x="*"

	for i in range(1,21):



		print(x*40)


elif pattern==2:

#Triangle-LeftAngled


	y="*"

	n=20

	a=0

	for i in range(1,21):


		print(y*(i+a), " "*n)

	
		n-=1

		a+=1

elif pattern==3:


#Triangle-RightAngled


	z="*"

	n=39


	b=1

	for i in range(1,21):

		
	
		print(" "*(n), z*(b))

		b+=2

		n-=2	

elif pattern==4:


#Triangle




	w="*"

	n=20

	m=1

	for i in range(1,21):

		print(" "*n,w*m)

		n-=1
	
		m+=2


#HourGlass

elif pattern==5:


	q="*"

	e=1

	f=39

	k=20

	for i in range(1,21):

		print(" "*e,q*f)

		e+=1

		f-=2

	e=1

	for j in range(1,21):

		print(" "*k,q*e)

		e+=2

		k-=1


else:

	print("Please enter correct option")


















