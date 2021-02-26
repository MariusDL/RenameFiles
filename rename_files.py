#Rename all files in a folder in sequence

import os 
   
word = input("Enter a word to put in front of the numbers or press enter: ")
word = str(word)

count = input("Enter the number you want to start the count from: ")

# check if input is a digit
if count.isdigit() == False:
    count = "1" 

# check if input entered otherwise start from 1
if len(count) == 0:
    count = 1

count = int(count)
count = abs(count)

if len(word) == 0:
    word=""

#get current directory
path = os.getcwd()


#iterate throughout all files in the current directory 
for x, filename in enumerate(os.listdir(path)):

    #keep the name of the script
    if filename == "rename_files.py":
        continue
    
    #get the extension of the file to keep it the same
    root, extension = os.path.splitext(filename)

    #new name of the file    
    new_name = word + str(count) + extension

    #rename the file    
    os.rename(filename, new_name)

    #increment count
    count = count + 1
        
print("All files have been successfully renamed")
