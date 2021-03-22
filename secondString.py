
#Takes a sentence and outputs every second letter in reverse order.


sentence = input('Please enter a sentence:') # Reads in the input and assigns the variable.

newstring = sentence[::-2]  #Takes in the arguements of the string ['a','b',...] and returns in increments of 2 going backwards. 
print(newstring) #Output to the user. 


#https://www.w3schools.com/python/python_howto_reverse_string.asp
#Solution to slicing a string.


#https://www.programiz.com/python-programming/methods/built-in/slice
# This site gave the best explanation for how this method works.  
# string[start:stop:step] 
# In my case I take the default start and stop are the defaults and I increment going backwards by - 2. 


#https://www.w3schools.com/python/python_strings.asp
# Useful to understand the datatpye of a string (an array)
