import numpy as np
import matplotlib.pyplot as plt



x = np.linspace(0, 4, num = 1000, endpoint= True)  # interval is [0,4] on the number line, lenght of arraty is 1000, and I include the endpoint in the array. 
fx = x # returns an array y =  (0,0.006,0.012, ...5)
gx = x*x # return an attay y = (0,0.006^2,...)
hx = x*x*x



#https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
# I closely follow this the guide from the documentation website. 

plt.plot(x,fx, label = 'f(x)=x') # plot each of the functions.  
plt.plot(x,hx, label = 'g(x)=x^2') 
plt.plot(x,gx, label = 'h(x)=x^3')
plt.title("My Plot")
plt.legend()
plt.show()git





#https://www.tutorialspoint.com/numpy/numpy_matplotlib.htm
#https://matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
#-> How to make nice graphs

#https://scipy-lectures.org/intro/numpy/operations.html
#-> How operations are performed on arrays. x+a = (x1+a,x2+a,..) 
# x*x= (x1*x1,X*2*x2,...)




#https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange
#https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace

#resources to generate x values for a smoother graph. 