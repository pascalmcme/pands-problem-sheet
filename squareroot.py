
#a^(1/2) = x
# x^2 = a
# We can write as when is f(x) = x^2 - a = 0, where a is the number we want the root of
# Apply Newton's method to approximate values that solve the function. 

#x_(n+1) = x_n - ( f(x_n) / f' (x_n) )

Number = int(input('Please enter a postive number: '))
guess = 1 # guess
maxIterations = 10

def newtonsMethod(Number):
 x0 = guess
 
 for i in range(maxIterations):
  fx = x0**2 - Number
  yprime = 2*x0  
  x1 = x0 - fx/yprime
  x0=x1

 return x1
 
 
  
 

print(newtonsMethod(Number))
  

     


 
  






