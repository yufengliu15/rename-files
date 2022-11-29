import functions

def main():
    while True:
        # os.getcwd() gets the Current Working Directory
        currDirectory = functions.getCwd()
        functions.clear()
        print (f"Current Directory: {currDirectory}") 

        directoryChange = functions.menu(["Remain in directory", "Change directories", "Print everything in this directory", "Quit"], "Improper input, try again")
        
        if directoryChange == 1:
            stringToRemove = input("What string would you like to remove from your files?: ")
            stringToReplace = input("What string would you like to replace it with?: ")
            
            functions.rename(currDirectory, stringToRemove, stringToReplace)
            print ("Rename successful!")
            
        elif directoryChange == 2:
            directoryChange = functions.menu(["Change directory forward", "Go back one directory"],"Improper input, try again")

            if directoryChange == 1:
                nextDir = currDirectory + input("Input the next file path: ")
                if functions.dirExists(nextDir):
                    functions.changeDir(nextDir)
                else:
                    print ("Directory does not exist")

            elif directoryChange == 2:
                functions.changeDir(functions.backwards(currDirectory))
                continue

        elif directoryChange == 3:
            functions.printDir(currDirectory)
        elif directoryChange == 4:
            break
        
        functions.delay(1)
                  
main()