
# provides tool to support command line arguements, for example sys.arg.
import sys 


# sys.argv[1] contains the first item on the list of command line arguements after the name of the python programme.
# the user will enter the python programme they wish to run "python es.py" followed by the text file "example.txt".
# Assign file name to the second input. 
filename = sys.argv[1]  

#this function takes file name and opens the conents in read mode.
def openFile(filename):  
    with open(filename,"rt") as f: #open the file in read text mode - name that file f
        data = f.read()  # f.read() reads the contents of the file and assings it to data.
        return(data) #want the function to return data, which is a string.

# this funtion counts the number of e's in a string
def editString(string): # takes the variable string as an input.
    numberOfEs = string.count("e") # string.count() counts the number of times a strring pattern "" appears in a string. 
    print(numberOfEs) #I also use the function to print the end result to the user.



openFile(filename) #call the openFile function, with filename as the input.
string = openFile(filename) #assign the string variable as the text from that file
editString(string) #call the editString funtion to return the number of e's from the string and show the output to the users





#https://realpython.com/python-command-line-arguments/#file-handling
#reference for using command additional command line arguements

#https://www.w3schools.com/python/ref_string_count.asp  - 
# reference for editing string