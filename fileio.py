# FILE IO CONSISTS OF TWO METHOD


# BY MANUALLY OPENING FILE IN ANY OF MODE BUT NEEDS TO BE CLOSED ALL THE TIME.
''' 
 1)   'r': Read mode (Default). Opens text for reading; errors out if missing. 
 2)   'w': Write mode. Overwrites existing text or creates a new file. 
 3)   'a': Append mode. Appends new text to the end without deleting old data. 
 4)   'x': Exclusive creation. Fails explicitly if the file already exists. 
 5)   'b': Binary mode. Used alongside other modes (e.g., 'rb', 'wb') for images or executables. 
 6)   '+': Update mode. Allows simultaneous reading and writing (e.g., 'r+') 
 
BUT ALWAYS REMEMBER TO CLOSE THE FILE IN THE END!
'''



# READING FILE
'''
fyle = open('file0.txt','r')   # when there is none, there is rt 'by-default' for reading text
                               # 'rb'- opens the file to read in binary eg(image, jpeg, pdf, exe.) 
print(fyle)
text = fyle.read()
print(text)
fyle.close()  # CLosing the file is mandatory 

'''
# WRITING FILE
'''

f.write("this overwrited the prior text")
f = open('file0.txt', 'a')
f.write("this appends the text in the file without overwriting it")
f.close() 
'''

# 'WITH' FUNCTION CLOSES THE 'FILE' BY-DEFAULT
'''
with open('file0.txt','a+') as fyle:
    fyle.write('text is getting added to the "file0.txt"\n')
    fyle.seek(1)
    print(fyle.read())
'''
# READLINE function
f = open('file0.txt', 'r')
while True:
    line = f.readline()
    print(line)
    if not line:
        break