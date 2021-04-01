
#Takes a sentence and outputs every second letter in reverse order

#User is prompted for a sentence. Their input is then assigned to the sentence variable.
sentence = input('Please enter a sentence:') 

#the newstring reverses the sentence string and returns every second letter. 
#[::-2] string slice, select the elements from the string array.Start and stop are the defaults and I increment going backwards by - 2.
newstring = sentence[::-2] 

#return the correct output (newstring) to the user. 
print(newstring) 






#https://www.w3schools.com/python/python_howto_reverse_string.asp
#Solution to slicing a string.


#https://www.programiz.com/python-programming/methods/built-in/slice
# This site gave the best explanation for how this method works.  
# string[start:stop:step] 



#https://www.w3schools.com/python/python_strings.asp
# Useful to understand the datatpye of a string (an array)
