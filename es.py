
import sys

#opts = [opt for opt in sys.argv[1:] if opt.startswith(" ")]
#args = [arg for arg in sys.argv[1:] if not arg.startswith(" ")]



filename = sys.argv[1]

def openFile(filename):
    with open(filename,"rt") as f:
        data = f.read()
        return(data)


def editString(string):
    numberOfEs = string.count("e")
    print(numberOfEs)



openFile(filename)
string = openFile(filename)
editString(string)





#https://realpython.com/python-command-line-arguments/#file-handling

#https://www.w3schools.com/python/ref_string_count.asp  - count string