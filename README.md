# pands-problem-sheet

# BMI.py 
This program calculates the user's BMI. The user enters their height and weight when prompted and the value for their BMI is returned. 

The program works by using built in operators, multiplication and division, to create a BMI variable from height and weight.


# secondString.py
This program takes and input sentence from the user. It reversed the order of the sentence and returns every second letter. 

The program works by storing the sentence as a string. A new string is then created by slicing the original string backwards in 
increments of two. Finally, the new string is returned. 



# collatz.py
This program takes positive integer from the user. If the number is odd, it is multiplied by three and one is added.
If the number is even, it is divided by two. The new number is then added to the sequence and the process is repeated
for the new number. The process continues until the new number is equal to one. The sequence of numbers is then returned to the user.

The program works by creating a list for the numbers to be stored in. The first number of the list is given by the user and it is also used 
as the first value in the loop. A while loop is used to perform the operations as we want the loop to end when the new number is equal to one. 
Within the loop the operation to be performed depends on the value that enters it (even or odd). If and else statements are used 
to deal with the two cases. The arithmetic is then performed and the new number is appended to the list. When the loop is completed the list is returned. 

# datetime.py

This program lets the user know the day of the week and whether or not it is a weekday, when they run the program. 

The program uses the datetime module is used with the function date.today() which return the current date. This date is then formatted. To return the day of the week 
I format the date to only show the day. To show whether or not the it is a weekday I format the day of the week as a number (0-6), with 6 and 0 indicating Saturday 
and Sunday. If and Else statements are used to used in combination with the weekday number to give the correct notification. 

# squareroot.py
This program takes a positive float and returns an approximation of it's square root. It uses Newton's method to return values which get closer and
closer to solving for x^2 = a , where a is the number we want the square root of. The process can be summarised by the formula below, with x_(n+1)
being a better approximation then x_n
x_(n+1) = x_n - ( f(x_n) / f' (x_n) )

The program works creating a function which applies this recursive method to the number that user enters. The initial guess x0 is arbitrary and
set to one, and is used to initialise the loop. x1 is then calculated with the above formula. X0, the value that starts the loop is then set to
be equal to x1, and is used to get the next x1, or x_(n+1). I use a for loop for this to repeat the process ten times. The function then returns the final 
x1, the best approximation. This function is then called and the result displayed to the user. 


# es.py
This program takes two inputs from the command line, the name of the program file and the example.txt file. It counts the number of e's and returns 
this to the user.

The program uses the sys module to allow for additional inputs from the command line. The program specifies the file name to be opened as the second 
input on the command line, for example es.py example.txt. Two additional functions are added by the program. The first opens the file in read mode and
returns the text inside as a string. The second function counts the number of times the letter e occurs. The result of this function is returned to the user.


# pplottask.py
this programme plots the function f(X) = x, g(X)=x^2 and h(x)=x^3 in the range [0,4]. 

The program uses two modules, numpy for additional tools to work with arrays, and matplotlib.pyplot for plotting tools. The program first creates the x points,
1000 of them between on the interval [0,4]. The functions values, y, are then created, based on array operations. For example g(x) = [x1^2,x2^",...x1000^2]. 
The functions offered my mayplotlib are then used to plot these functions and display them to the user. 










