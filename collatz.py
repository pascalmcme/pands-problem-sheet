

numbers = [] #create a list called numbers
numbers.append(number) #To include the initial variable I first append the original number to the list.


number = int(input('Please enter a positive integer:'))  #Initialise the loop. 


while number !=1:  # Creats a loop that stops when number = 1 
 if number % 2 == 0: # If Even                 
   number = int(number / 2) # operation if the number is even
 else: # If odd
    number = int((number * 3)+1) # operation if the number is odd
 numbers.append(number)  # Import to put this in the while loop, otherwise just left with the "1" in list


print(numbers) #show output


# https://www.w3schools.com/python/python_lists_add.asp 
# https://www.programiz.com/python-programming/methods/list/append

# Reference for appending items to a list. 


# https://www.w3schools.com/python/python_while_loops.asp


# Reference for using a while loop. 