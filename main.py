import os, functions

def rename(stringToRemove, stringToAdd):
    os.rename(stringToRemove,stringToAdd)
    
def backwards(filePath):
    occurences = []
    for i in range(len(filePath)):
        if filePath[i] == "/":
            occurences.append(i)
    
    lastOccurence = occurences[len(occurences)-1]
    return filePath[:lastOccurence]

def askUserRename():
    stringToRemove = input("What string would you like to remove from your files? ")
    stringToAdd = input("What string would you like to replace it with? ")
    return stringToRemove, stringToAdd

def main():
    while True:
        # os.getcwd() gets the Current Working Directory
        currDirectory = os.getcwd()
        print (f"Current Directory: {currDirectory}") 
        print (".. to remain in directory, -q to quit, cd to change directory, .b to go back one directory")
        directoryChange = input("What would you like to do?")

        if directoryChange == "cd":
            os.chdir(currDirectory + input("Input the file path: "))
        elif directoryChange == "-q":
            break
        elif directoryChange == ".b":
            os.chdir(backwards(currDirectory))
            continue
        elif not(directoryChange == ".."):
            print ("Improper input, try again")
            continue
        
        stringToRemove, stringToAdd = askUserRename()
        rename(stringToRemove, stringToAdd)
        
               
main()