#!/bin/bash


echo "this is a test script"

echo "enter the marks obtained"

declare -i x

x=75

echo "Marks obtained : $x"

if [[ x -gt 80 ]]

then

   echo "choose mbbs"

elif [[ x -gt 70 ]]

then

   echo "choose engineering"

else

   echo "choose commerce"

fi



