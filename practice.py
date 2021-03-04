number = int(input('Please enter a positive integer:'))

if number % 2 == 0:
    print('number is even')
elif number % 2 != 0:
 print('number is odd')






 
Number = int(input('Please enter a postive number: '))
#a^(1/2) = x
# x^2 = a
# We can write as when is f(x) = x^2 - a = 0, where a is the number we want the root of
# Apply Newton's method to approximate values that solve the function. 

#x_(n+1) = x_n - ( f(x_n) / f' (x_n) )

guess = 1



def newtonsMethod(Number):
 
 x0 = 1 # guess
 
 for i in range(9):
  fx = x0**2 - Number
  yprime = 2*x0
  x1 = x0 - fx/yprime
  x0 = x1
 return x0
  
  
  


  

answer = newtonsMethod(Number)  # get result from the funtion

print(answer)  # display result

