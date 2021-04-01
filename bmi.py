#Calculate BMI when the user inputs height and weight.


# recieves the input after promting the user to enter height. Stores this value as a float. Assigns that value to the Height variable.
height = float(input('Enter Height:')) 

#  same as for Height
weight = float(input('Enter Weight:'))

#BMI = kg/(m^2). Assign the BMI variable. It is a function of the height and weight variables. 
BMI = weight / (height*height) 

#Print returns the output to the user. This prints a string "Your BMI is" and the value for BMI. format() is used to deal with the two data tpyes (string and float)
print("Your BMI is {}". format(BMI))  




#https://www.w3schools.com/python/python_datatypes.asp
#Information about specifying a data type.  


#https://www.w3schools.com/python/python_operators.asp
#Information about operators, to perform BMI calculation and for comparison operators. 