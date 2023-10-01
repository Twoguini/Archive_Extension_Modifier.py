import os
import re

#SECTION: Priority List:
#NOTE: 1° - Finish Functionality
#NOTE: 2° - Turn Code Into Funcions
#NOTE: 3° - Test Routine
#NOTE: 4° - State Variables
#!SECTION

#TODO: State all used global variables 
choosed_Files: str = []
loop_Controller: int = 0
file_Names: list = []
target_Files: list = []

# Asks for the File Path
directory_Path: str = os.path.normpath(input('Insert the path of the target: \n'))

def counting_Files(directory_Path: str) -> int:
    ''' Returns a Int with the count of how many files there are into the directory '''
    number_of_Files: int = 0
    
    # Runs for every file in the dir
    for path in os.listdir(directory_Path):
        
        # Checks if it is a file or a subdir and, if it is a file, counts it
        if (os.path.isfile(os.path.join(directory_Path, path))):
            number_of_Files += 1
    
    # Returns the output
    return ('Your dir has: {0} files'.format(number_of_Files))

#TODO: Finish main functionality
def modify_Extension(target, directory_Path):
    ''' Main objective! Changes the file extension by changing its after "." charactres '''
    splitedTargetNameAndExtension = os.path.splitext(directory_Path)
    name = splitedTargetNameAndExtension[0]
    
 
# Checks if it exists
# If exists
if (os.path.exists(directory_Path) != False): 
    print(directory_Path)

    # Checks if it is a Dir or a File
    # If File
    if(os.path.isfile(directory_Path)):
        modify_Extension(directory_Path,directory_Path)

    # If Dir
    else:
        
        # Checks if the given dir is empty or not
        if(os.path.getsize(directory_Path) == 0):
            print('Thats a empty dir')
            
        else:
            
            # Stores the names of those files into a var, only if it is a file.
            all_Files_Names = os.scandir(directory_Path)
            for i in all_Files_Names:
                if (i.is_dir()):loop_Controller += 1
                else:
                    file_Names.append(os.listdir(directory_Path)[loop_Controller])
                    loop_Controller += 1
            loop_Controller = 0
            
            # Prints on screen the number os files
            print(counting_Files(directory_Path))

            # lists files 
            for i in file_Names:
                print('*{0} - {1}'.format(loop_Controller+1, file_Names[loop_Controller]))
                loop_Controller += 1
            loop_Controller = 0

            # Let the user choose which files he wants to modify
            choosed_Files = input('Insert the number of the target: \n(Use : between 2 numbers to indicate a range) \n')

            # Handles letter between choices error
            try:
                
                # Stores the separated targets into a Array, excluding duplicates
                raw_Splitted_Choices = list(set(re.split(' |,|-', choosed_Files)))

                #TODO: Turn massive chunks of code, like this one, into as many functions as possible.

                # Identify if there is a : between numbers, if true, target files in range
                for i in raw_Splitted_Choices:
                    if (':' in raw_Splitted_Choices[loop_Controller]):
                        raw_Splited_Range_OPT = raw_Splitted_Choices[loop_Controller].split(':')
                        splited_Range_OPT_as_Int = [int(i) for i in raw_Splited_Range_OPT]
                        raw_Splitted_Choices.remove(raw_Splitted_Choices[loop_Controller])
                        first_File_in_Range = min(splited_Range_OPT_as_Int)
                        last_File_in_Range = max(splited_Range_OPT_as_Int)
                        second_Loop_Controller = 0
                        file_Range = (last_File_in_Range - first_File_in_Range)
                        raw_Splitted_Choices.append(str(last_File_in_Range))
                        print(file_Range, last_File_in_Range, first_File_in_Range, raw_Splited_Range_OPT)
                        while (second_Loop_Controller < file_Range):
                            raw_Splitted_Choices.append(str(first_File_in_Range))
                            first_File_in_Range += 1
                            second_Loop_Controller += 1
                            print(second_Loop_Controller, file_Range)
                    loop_Controller += 1
                loop_Controller = 0

                # Deletes blank cases
                for i in raw_Splitted_Choices:
                    if (raw_Splitted_Choices[loop_Controller] == ''):
                        raw_Splitted_Choices.remove(raw_Splitted_Choices[loop_Controller])
                        loop_Controller +=1
                loop_Controller = 0

                # Print the target names
                for i in raw_Splitted_Choices:
                    list_Value_Indexer = int(raw_Splitted_Choices[loop_Controller])
                    loop_Controller += 1
                    print(file_Names[list_Value_Indexer-1])
                    target_Files.append(file_Names[list_Value_Indexer-1])
                   
            # Case an error occours
            except:
                print('Use only numbers')
    
         
# If not
else: 
    print('Could not locate it\n')

# TODO: Create test routines