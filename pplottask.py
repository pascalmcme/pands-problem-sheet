import numpy as np # import tools to work with arrays.
import matplotlib.pyplot as plt # import tools which support creating plots.




# assign the x values. This is an array on the interval [0,4], its lenght is 1000, and I include the endpoint in the array. 
x = np.linspace(0, 4, num = 1000, endpoint= True)   
# array operations are perfomed as follows: x*x= (x1*x1,X*2*x2,...)
fx = x # returns an array y =  (0,0.006,0.012, ...5) f(x) = x
gx = x*x # return an array y = (0,0.006^2,...) g(x) = x^2
hx = x*x*x # h(x) = x^3



#https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
# Apply the plt.plot() funtions to create the different parts of the plot.

plt.plot(x,fx, label = 'f(x)=x') # plot each of the functions (x,y,label)
plt.plot(x,hx, label = 'g(x)=x^2') 
plt.plot(x,gx, label = 'h(x)=x^3')
plt.title("My Plot") # create a title
plt.legend() # add a legend
plt.show() # display the plot
#plt.savefig("myplot.jpg") # save the plot





#https://www.tutorialspoint.com/numpy/numpy_matplotlib.htm
#https://matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
#-> How to make nice graphs

#https://scipy-lectures.org/intro/numpy/operations.html
#-> How operations are performed on arrays. x+a = (x1+a,x2+a,..) 
# x*x= (x1*x1,X*2*x2,...)




#https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange
#https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace

#resources to generate x values for a smoother graph. 