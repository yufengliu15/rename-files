import os,time

def delay(timeInSeconds):
    time.sleep(timeInSeconds)
    return

def rename(_currDir, _stringToRemove, _stringToReplace):
    for file in os.listdir(_currDir):
        splitFileName = os.path.splitext(file)
        fileName = splitFileName[0]
        fileExtension = splitFileName[1]
        
        if _stringToRemove in fileName:
            indexStart = fileName.find(_stringToRemove)
            indexEnd = indexStart + len(_stringToRemove)
            newName = fileName[:indexStart] + _stringToReplace + fileName[indexEnd:] + fileExtension
            os.rename(file, newName)
    return   
    
def getCwd():
    return os.getcwd()    

def clear():
    os.system("clear")
    return

def dirExists(_currDir):
    return os.path.exists(_currDir)
    
def changeDir(_currDir):
    os.chdir(_currDir)
    return 
    
def backwards(filePath):
    print (filePath)
    occurences = []
    for i in range(len(filePath)):
        # "/ for mac, \ for windows"
        if filePath[i] == "/" or filePath[i] == "\\":
            occurences.append(i)
    
    lastOccurence = occurences[len(occurences)-1]
    return filePath[:lastOccurence]

def menu(listOfOptions, errorMessage):
    counter = 1
    for options in listOfOptions:
        print (f"{counter}. {options}")
        counter += 1
    
    while True:
        userChoice = input(": ")

        try:
            if (int(userChoice) > (len(listOfOptions))) or (int(userChoice) < 1):
                print (errorMessage)
            else:
                break
        except:
            print (errorMessage)
    return int(userChoice)

def printDir(_currDir):
    for file in os.listdir(_currDir):
        print (file)
    return