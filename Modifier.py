import os
import re

#SECTION: Priority List:
#ANCHOR: DONE 
#NOTE: 1° - Finish Functionality
#ANCHOR: DONE
#NOTE: 2° - Turn Code into Functions
#NOTE: 3° - Reorgzanize and comment code. State All Variables, their types, comment functions and set their return types
#NOTE: 4° - Give better looking prints and ui
#NOTE: 5° - Test Routine
#!SECTION

#SECTION: Variables
#TODO: State all used global variables 
choosed_Files: str = []
loop_Controller: int = 0
file_Names: list = []
target_Files: list = []
#!SECTION

# Asks for the File Path
directory_Path: str = os.path.normpath(input('Insert the path of the target: \n'))

#SECTION: Functions

#SECTION: Function to count files
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
#!SECTION

#SECTION: Function to store files name and print'em 
def storing_Files_Name(d_Path, loop_Controller):
    all_Files_Names = os.scandir(d_Path)
    for i in all_Files_Names:
        if (i.is_dir()):loop_Controller += 1
        else:
            file_Names.append(os.listdir(directory_Path)[loop_Controller])
            loop_Controller += 1
    loop_Controller = 0
    for i in file_Names:
        print('*{0} - {1}'.format(loop_Controller+1, file_Names[loop_Controller]))
        loop_Controller += 1
#!SECTION

#SECTION: Files range option
def range_Option(choices, loop_Controller):
    for i in choices:
        if ('-' in choices[loop_Controller]):
            raw_Range_OPT = choices[loop_Controller].split('-')
            range_OPT_Int = [int(i) for i in raw_Range_OPT]
            choices.remove(choices[loop_Controller])
            first_in_Range = min(range_OPT_Int)
            last_in_Range = max(range_OPT_Int)
            second_Loop_Controller = 0
            file_Range = (last_in_Range - first_in_Range)
            choices.append(str(last_in_Range))
            while (second_Loop_Controller < file_Range):
                choices.append(str(first_in_Range))
                first_in_Range += 1
                second_Loop_Controller += 1
        loop_Controller += 1
#!SECTION

#SECTION: Function to delete blank characteres
def deleting_Blank(raw_Splitted_Choices, loop_Controller):
    for i in raw_Splitted_Choices:
        if (raw_Splitted_Choices[loop_Controller] == ''):
            raw_Splitted_Choices.remove(raw_Splitted_Choices[loop_Controller])
            loop_Controller += 1
#!SECTION

#SECTION: Function to store choices
def storing_Choices(raw_Splitted_Choices, loop_Controller) -> list:
    for i in raw_Splitted_Choices:
        list_Value_Indexer = int(raw_Splitted_Choices[loop_Controller])
        loop_Controller += 1
        print(file_Names[list_Value_Indexer-1])
        target_Files.append(file_Names[list_Value_Indexer-1])
    return(target_Files)
#!SECTION

#SECTION: Function to separate file names from extensions
def separate_File_Name(target):
    loop_Controller = 0
    name: str = ""

    splited_Target = target.split('.')
    splited_Max = len(splited_Target) - 1

    while loop_Controller < splited_Max:
        if (loop_Controller > 0):
            name += ('.'+splited_Target[loop_Controller])
        else:
            name += splited_Target[loop_Controller]
        loop_Controller += 1
    extension = splited_Target[len(splited_Target)-1]
    return name, extension
#!SECTION

#SECTION: Main function, to modify the files extension
def modify_Extension_inDir(target, path):
    ''' Main objective! Changes the file extension by changing its after "." charactres '''
    file_New_Extention = input("digite a nova extensão: (Use . before it)\n")
    for i in target:
        file_Past_Name = path + "/" + i
        file_New_Name = path + "/" + separate_File_Name(i)[0] + file_New_Extention
        print("File {0} was changed to {1}".format(file_Past_Name, file_New_Name))
        os.rename(file_Past_Name, file_New_Name)
#!SECTION

#SECTION: Function to modify extension from file inside the given path
def modify_Extension_Direct_Path(file_Past_Name):
    file_New_Extention = input("digite a nova extensão: (Use . before it)\n")
    file_New_Name = separate_File_Name(file_Past_Name)[0] + file_New_Extention
    print("File {0} was changed to {1}".format(file_Past_Name, file_New_Name))
    os.rename(file_Past_Name, file_New_Name)
#!SECTION

#!SECTION

# Checks if it exists
# If exists
if (os.path.exists(directory_Path) != False): 
    print(directory_Path)

    # Checks if it is a Dir or a File
    # If File
    if(os.path.isfile(directory_Path)):
        modify_Extension_Direct_Path(directory_Path)

    # If Dir
    else:
        
        # Checks if the given dir is empty or not
        if(os.path.getsize(directory_Path) == 0):
            print('Thats a empty dir')
            
        else:
            
            # Prints on screen the number os files
            print(counting_Files(directory_Path))

            storing_Files_Name(directory_Path, loop_Controller = 0)

            # Let the user choose which files he wants to modify
            choosed_Files = input('Insert the number of the target: \n(Use : between 2 numbers to indicate a range) \n')

            # Handles letter between choices error
            try:
                
                # Stores the separated targets into a Array, excluding duplicates
                raw_Splitted_Choices = list(set(re.split(' |,|:|;', choosed_Files)))

                range_Option(raw_Splitted_Choices, loop_Controller = 0)

                deleting_Blank(raw_Splitted_Choices, loop_Controller = 0)

                storing_Choices(raw_Splitted_Choices, loop_Controller = 0)

                modify_Extension_inDir(target_Files, directory_Path)
                    
            # Case an error occours
            except:
                print('Invalid Numbers')
         
# If not
else: 
    print('Could not locate it\n')

# TODO: Create test routines