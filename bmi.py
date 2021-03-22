#Calculate BMI when the user inputs height and weight.

Height = float(input('Enter Height:'))  # Assign the variable height to the users input for height.
Weight = float(input('Enter Weight:')) # Store values as floats since height and weight can take decimal values. 



BMI = Weight / (Height*Height) #BMI = kg/(m^2)



print("Your BMI is {}". format(BMI))  #Returns output to user. Use format because we are printing two data types. 

#https://www.w3schools.com/python/python_datatypes.asp
#Information about specifying a data type.  


#https://www.w3schools.com/python/python_operators.asp
#Information about operators, to perform BMI calculation and for comparison operators. 