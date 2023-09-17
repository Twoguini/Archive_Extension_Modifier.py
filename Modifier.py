import os

choices = []
next = 0
files = []

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


#Checks if it exists
#If exists
if (os.path.exists(caminho) != False): 
    print(caminho)

    #Checks if it is a Dir or a File
    #If File
    if(os.path.isfile(caminho)):
        print(os.path.splitext(caminho))

    #If Dir
    else:
        #Checks if the given dir is empty or not
        if(os.path.getsize(caminho) == 0):
            print('Thats a empty dir')
            
        else:
            #Stores the list of files into a var
            for x in os.listdir(caminho):
                files.append(os.listdir(caminho)[next])
                next += 1
            next = 0 

            print(countFiles(caminho))

            #lists files 
            for x in files:
                print('*{0} - {1}'.format(next+1, files[next]))
                next += 1
            next = 0

            #Let the user choose which files he wants to modify
            choices = input('Insert the number of the target (if more than 1, use spaces between the numbers): \n')

            #Stores the targets into a Array
            point = choices.split()
            
            #Print the target names
            for x in point:
                arrayPosition = int(point[next])
                next += 1
                print(files[arrayPosition-1])


    
#If not
else: 
    print('Could not locate it\n')
