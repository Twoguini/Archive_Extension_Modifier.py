import os
import re

choices = []
next = 0
files = []
targetFiles = []

#Asks for the File Path
caminho = os.path.normpath(input('Insert the path of the target: \n'))

#Counts how many files there are into the dir
def countFiles(caminho):
    filecount = 0
    
    #Runs for every file in the dir
    for path in os.listdir(caminho):
        
        #Checks if it is a file or a subdir and, if it is a file, counts it
        if (os.path.isfile(os.path.join(caminho, path))):
            filecount += 1
    
    #Returns the output
    return ('Your dir has: {0} files'.format(filecount))

def modifyExtension(target, caminho):
    splitedTargetNameAndExtension = os.path.splitext(caminho)
    name = splitedTargetNameAndExtension[0]
    
        


#Checks if it exists
#If exists
if (os.path.exists(caminho) != False): 
    print(caminho)

    #Checks if it is a Dir or a File
    #If File
    if(os.path.isfile(caminho)):
        modifyExtension(caminho,caminho)

    #If Dir
    else:
        
        #Checks if the given dir is empty or not
        if(os.path.getsize(caminho) == 0):
            print('Thats a empty dir')
            
        else:
            
            #Stores the names of those files into a var, only if it is a file.
            scanner = os.scandir(caminho)
            for entry in scanner:
                if (entry.is_dir()):next += 1
                else:
                    files.append(os.listdir(caminho)[next])
                    next += 1
            next = 0
            
            #Prints on screen the number os files
            print(countFiles(caminho))

            #lists files 
            for x in files:
                print('*{0} - {1}'.format(next+1, files[next]))
                next += 1
            next = 0

            #Let the user choose which files he wants to modify
            choices = input('Insert the number of the target: \n(Use : between 2 numbers to indicate a range) \n')

            #Handles letter between choices error
            try:
                
                #Stores the separated targets into a Array, excluding duplicates
                splitedChoices = list(set(re.split(' |,|-', choices)))

                #Identify if there is a : between numbers, if true, target files in range
                for x in splitedChoices:
                    if (':' in splitedChoices[next]):
                        splitedChoicesThrougthOPT = splitedChoices[next].split(':')
                        splitedChoicesThrougthOPTConverted = [int(i) for i in splitedChoicesThrougthOPT]
                        splitedChoices.remove(splitedChoices[next])
                        firstFileValue = min(splitedChoicesThrougthOPTConverted)
                        secondFileValue = max(splitedChoicesThrougthOPTConverted)
                        counter = 0 
                        counterRange = (secondFileValue - firstFileValue)
                        splitedChoices.append(str(secondFileValue))
                        print(counterRange, secondFileValue, firstFileValue, splitedChoicesThrougthOPT)
                        while (counter < counterRange):
                            splitedChoices.append(str(firstFileValue))
                            firstFileValue += 1
                            counter += 1
                            print(counter, counterRange)
                    next += 1
                next = 0

                #Deletes blank cases
                for x in splitedChoices:
                    if (splitedChoices[next] == ''):
                        splitedChoices.remove(splitedChoices[next])
                        next +=1
                next = 0

                #Print the target names
                for x in splitedChoices:
                    arrayPosition = int(splitedChoices[next])
                    next += 1
                    print(files[arrayPosition-1])
                    targetFiles.append(files[arrayPosition-1])
                   
            #Case an error occours
            except:
                print('Use only numbers')
    
         
#If not
else: 
    print('Could not locate it\n')
