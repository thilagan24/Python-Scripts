


declare -i x

echo "We are going to check the Voting eligibility"

echo "Please enter your age:"

read x

if [[ x -ge 18 ]];

	then

		echo "You are eligible";

else

	echo "You are not eligible";

fi
