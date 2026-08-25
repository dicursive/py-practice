with open ("seek&tellmethod.txt", 'r') as file:    
    # print(type(file))
    
    file.seek(5) 
#SEEK skips the letter wrt index given
    print(file.tell())
#tells the place
    data = file.read()
    print(data)
    
    # data = file.read(5) 
# reads the index wrt range 
    # print(file.tell())

with open("trunctated", "r") as file1:
    # file1.write("hello dude") 
    # file1.truncate(3)  
#truncate function decreases the text range to given value 
    print(file1.read())