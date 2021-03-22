


Number = int(input('Please enter a postive number: '))  # users input is assigned to the number variable
guess = 1 # we need an ititial guess of the square toor of number to apply newton's method

maxIterations = 10 # how many times we want to iterate the method

def newtonsMethod(Number):
 x0 = guess # the first value for x0 is the guess.
 
 for i in range(maxIterations): # use a for loop to repeat the process for specified number of times
  fx = x0**2 - Number #
  yprime = 2*x0  #
  x1 = x0 - fx/yprime # applying the recursive method to get x1, a closer guess to the square root of Number
  x0=x1 # x0 is updated so that we can start the loop again. 

 return x1  # when the loop is completed for the specified iterations the function returns x1, the best approximation for the root of Number. 

 
 


print(newtonsMethod(Number)) # prints the reult of the function newtonsMethod
  


#https://www.w3schools.com/python/python_for_loops.asp
#reference for using for loops. 

#https://www.w3schools.com/python/python_functions.asp
#reference for functions


#https://stackoverflow.com/questions/818828/is-it-possible-to-implement-a-python-for-range-loop-without-an-iterator-variable
# I could not think of a way to reference i in the loop. But I found this method was okay and used in one of the labs. 

#https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/newton/
#slightly different approach 









