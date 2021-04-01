
#create a list called numbers
numbers = [] 


#assign the number variable to the user's input.
#store it as an integer.
number = int(input('Please enter a positive integer:'))  


#To include the initial variable I first append the original number to the list with the append() function.
numbers.append(number) 


# This block of code repeats until the number is equal to one.
while number !=1:  # stops when the number is equal to one. 
 if number % 2 == 0: # If Even the indented operation is performed.              
   number = int(number / 2) # take number and divide by two.
 else: # If odd the indented operation is performed.
    number = int((number * 3)+1) # mutiply number by three and add 1.
 numbers.append(number)  # Important to append the number in while loop, otherwise just left with the "1" in list.


print(numbers) #show output, list of numbers


# https://www.w3schools.com/python/python_lists_add.asp 
# https://www.programiz.com/python-programming/methods/list/append

# Reference for appending items to a list. 


# https://www.w3schools.com/python/python_while_loops.asp


# Reference for using a while loop. 