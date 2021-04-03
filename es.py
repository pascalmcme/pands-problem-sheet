
# provides tools to support command line arguements, for example sys.arg.
import sys 


# sys.argv[1] contains the first item on the list of command line arguements after the name of the python programme.
# the user will enter the python programme they wish to run "python es.py" followed by the text file "example.txt".
# Assign file name to the second input. 
filename = sys.argv[1]  

#this function takes file name and opens the conents in read mode.
def openFile(filename):  # def function name: begins a function. Everything after must be indented. filename is the input.
    with open(filename,"rt") as f: #open the file in read text mode, need to get the text from file ,name that file f.
        data = f.read()  # f.read() reads the contents (text) from the file. Data is assigned to the result of the function.
        return(data) #want the function to return data when it runs, which is a string.

# this funtion counts the number of e's in a string
def editString(string): # takes the variable string as an input.
    numberOfEs = string.count("e") # string.count() counts the number of times a string pattern "e" appears in the string. 
    print(numberOfEs) #I also use the function to print the end result to the user.

# openFile(filename) #call the openFile function, with filename as the input. It returns the "data", the text from the file.
# editString(string) #call the editString funtion to return the number of e's from the result of openFile(). 
editString(openFile(filename))


# an alternative
# openFile(filename) 
# string = openFile(filename) 
# editString(string) 





#https://realpython.com/python-command-line-arguments/#file-handling
#reference for using command additional command line arguements

#https://www.w3schools.com/python/ref_string_count.asp  - 
# reference for editing string