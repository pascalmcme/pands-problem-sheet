

#import a module which allows to manipulation of dates and times
import datetime 
#Assing current date from datetime.now() function to date variable
date = datetime.datetime.now() 
#Create a variable today, takes todays date variable and applied strftime("%A")
#This function formats the date to only show the name of the day.  
today = date.strftime("%A")  
#print the output.
print('today is {}'.format(today))

# want weekdays as numbers so that I can use comparisons (start from 0 = Sunday)
# apply strftime("%w") to date to get the weekday number and assign it to the weekdaynumber variable.
weekdaynumber = date.strftime("%w")  
# If today is saturday or sunday it will print the indented line.
if weekdaynumber == 6  or weekdaynumber == 0:
    print("It is the weekend! Hoora!") 
# if today is a weekday it will print the indented line,   
else:
     print("Today is weekday! Yay!") #Otherwise print this



#https://www.programiz.com/python-programming/datetime/current-datetime
#https://www.w3schools.com/python/python_datetime.asp

# reference for the datetime module