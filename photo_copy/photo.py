import os # for working with files
import shutil # for copying files

print(os.getcwd())  # get current work directory
os.chdir('.') # change direcory
print(os.listdir()) # lists everything in a file

for dir in os.listdir(): # for each file in the opend directory
    if not dir.__contains__('.'): # do only if a folder doesnt have a dot '.' in its name 
        os.chdir(dir)  # go IN each folder
        for file in os.listdir():  # each file in each folder
            if file.__contains__('htmlimage'):   # searchinf for files containing 'htmlimage' 
                collection = file[11]  # creating a variable from the 11th element of the found file
                collection_dir = '../new photo' + '/' + collection  # creating a variable - direction, final destination - newly created folder (from the 11th el)
                
                if not os.path.exists(collection_dir): # if such direction doesnt exist
                    os.mkdir(collection_dir) # create it
                shutil.copy2(file, collection_dir) # copy the file to a new folder
                 
       
        os.chdir('..')

