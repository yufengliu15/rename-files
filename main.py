import functions

def main():
    while True:
        # os.getcwd() gets the Current Working Directory
        currDirectory = functions.getCwd()
        functions.clear()
        print (f"Current Directory: {currDirectory}") 
        print ("-q to quit")
        directoryChange =  input("Remain in directory? (y/n): ").lower()
        
        if directoryChange == 'y':
            stringToRemove = input("What string would you like to remove from your files?: ")
            stringToReplace = input("What string would you like to replace it with?: ")
            
            functions.rename(currDirectory, stringToRemove, stringToReplace)
            print ("Rename successful!")
            
        elif directoryChange == 'n':
            directoryChange = input("cd to change directory forward, .b to go back one directory: ").lower()
            if directoryChange == "cd":
                nextDir = currDirectory + input("Input the next file path: ")
                if functions.dirExists(nextDir):
                    functions.changeDir(nextDir)
                else:
                    print ("Directory does not exist")
            elif directoryChange == ".b":
                functions.changeDir(functions.backwards(currDirectory))
                continue
            else:
                print ("Improper input, try again")   
        elif directoryChange == "-q":
                break
        else:
            print ("Improper input, try again")
        
        functions.delay(1)
                  
main()