

#This program finds if the given year is leap year or not.

'''A year has exactly 365.2422 days

   To correct the 365 to 365.2422 days, we add/less days as below,

   Every 4th year, 1 day added i.e. 366 days, thus dividing by 4. This adds a day every 4 years. But this causes a drift.

   Below 2 steps are called century corrections, adds more precision towards the value 365.2422.

   Every Century/100th year, eg.1700,1800,1900,etc... ,. By dividing by 100, we skip a day every 100th year. 

   But, Every 400th year, eg.1200,1600,2000,etc. we make an exception of skipping as above. thus diving by 400. 

   This bring approximation of 365.2425 which is the closest we could attain to 365.2422'''


year=int(input("Please enter the year:"))


if year%4==0 and year%100!=0 or year%400==0:

    print("This given year is a leap year.")

else:

    print("The given year is not a leap year.")

    


