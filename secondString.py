
#Takes a sentence and outputs every second letter in reverse order.
#I followed the example and do not differentiate between letters and charachters.

sentence = input('Please enter a sentence:') # Reads in the input and assigns the variable.

newstring = sentence[::-2]  #Takes in the arguements of the string ['a','b',...] and returns in increments of 2 going backwards. 
print(newstring) #Output to the user. 


#https://www.w3schools.com/python/python_howto_reverse_string.asp
#source https://stackoverflow.com/questions/3453085/what-is-double-colon-in-python-when-subscripting-sequences