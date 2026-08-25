# OS Functions help in handling the file related scenarios
# such as creating bulk files, renaming them, finding the contents in the bulk files etc etc..

import os

if(not os.path.exists("DATA")):
    os.mkdir("DATA") # The mkdir function create a files in a directory and so a "DATA" will be 
    
# To create a bulk of files in DATA for some consecutive list

for i in range(0, 5): '''The range of number can be as much as wanted'''
'''The files till 5 are created'''
    # os.mkdir(f"DATA/file {i+1}") 


'''The files are renamed'''
    # os.rename(f"DATA/file {i+1}", f"DATA/FILE {i+1}")


'''The files contained in the 'DATA' is printed'''
folders = os.listdir("DATA") 
# print(folders)

# for folder in folders:
#     print(folder)

'''The content in the respective folders can also be excecuted'''

for folder in folders:
    print(os.listdir(f"DATA/{folder}"))