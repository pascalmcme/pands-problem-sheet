
import sys # provides tool to support command line arguements

#opts = [opt for opt in sys.argv[1:] if opt.startswith(" ")]
#args = [arg for arg in sys.argv[1:] if not arg.startswith(" ")]



filename = sys.argv[1]  # takes the file name from the second command line option. 


def openFile(filename):  # this function opens to read.
    with open(filename,"rt") as f:
        data = f.read()  # save the data/ text from the file
        return(data)


def editString(string): # this funtion counts the number of e's in a string
    numberOfEs = string.count("e")
    print(numberOfEs)



openFile(filename) #open the file
string = openFile(filename) #assign the string variable as the text from our file
editString(string) # we apply the funtion to return the number of e's





#https://realpython.com/python-command-line-arguments/#file-handling

#https://www.w3schools.com/python/ref_string_count.asp  - count string