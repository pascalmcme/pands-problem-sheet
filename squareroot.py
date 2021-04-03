

# users input is assigned to the number variable
Number = int(input('Please enter a postive number: '))  
# we need an ititial guess of the square root of number to apply newton's method.
# the initial guess should not be zero, or zero will be in the denominator in the function.

guess = 1 

# how many times we want to repeat the method
maxIterations = 10 


#create a funtion. It takes Number as the input and applies newton's method to approximate the square root.
def newtonsMethod(Number): 
 x0 = guess # the first value for x0 is the guess.
 # Use a for loop for iteration. This will repeat the proccess according to maxIterations.
 for i in range(maxIterations): 
  fx = x0**2 - Number # applying formula to solve for f(x)
  yprime = 2*x0 # applying formula to solve for f'(x)
  x1 = x0 - fx/yprime # applying the formula to get x1, a closer guess to the square root of Number
  x0=x1 # x0 is updated so that we can start the loop again.  

 return x1  # when the loop is completed for the specified iterations the function returns x1, the best approximation for the root of Number. 

 

print(newtonsMethod(Number)) # call the function newtonsMethod(Number) and print the result. 
  
# further explanation
# if no loop was used it would also be possible to solve for x2, x3 ...
# fx = x1**2
# yprime = 2*x1
# x2 = x1 - fx/yprime
# and repeat

#https://www.w3schools.com/python/python_for_loops.asp
#reference for using for loops. 

#https://www.w3schools.com/python/python_functions.asp
#reference for functions


#https://stackoverflow.com/questions/818828/is-it-possible-to-implement-a-python-for-range-loop-without-an-iterator-variable
# I could not think of a way to reference i in the loop. But I found this method was okay and used in one of the labs. 

#https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/newton/
#slightly different approach 









