

import datetime

date = datetime.datetime.now() #Returns the current date
today = date.strftime("%A")  #formats the date to give only the name of the day
print('today is {}'.format(today))


weekdaynumber = date.strftime("%w")  # want weekdays as numbers so that I can use comparisons (start from 0 = Sunday)
if today == 6  or today == 0:
    print("It is the weekend! Hoora!") # print this if today is Saturday or Sunday
else:
     print("Today is weekday! Yay!") #Otherwise print this



#https://www.programiz.com/python-programming/datetime/current-datetime
#https://www.w3schools.com/python/python_datetime.asp

# reference for the datetime module