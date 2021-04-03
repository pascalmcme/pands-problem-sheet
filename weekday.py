

#import a module which allows to manipulation of dates and times
import datetime 
#Assing current date from datetime.now() function to date variable
date = datetime.datetime.now() 
#Create a variable today, takes todays date variable and applied strftime("%A")
#This function formats the date to only show the name of the day.  
today = date.strftime("%A")  
#print the output.
print('today is {}'.format(today))


# If today is saturday or sunday it will print the indented line.
# or operator means if function is applied if one of these conditions are met. 
if today == "Saturday"  or today == "Sunday":
    print("It is the weekend! Hoora!") # output to user
#  when the if condition is not met, else is applied.    
else:
     print("Today is weekday! Yay!") # output to user



#https://www.programiz.com/python-programming/datetime/current-datetime
#https://www.w3schools.com/python/python_datetime.asp

# reference for the datetime module