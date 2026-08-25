
# Local vs global variables 

'''When a variable is defined outside any function then its a GLOBAL VARIABLE'''
x = 9
y = "NINE"

'''SIMILARLY, when a variable is defined inside the function then its a LOCAL VARIABLE'''

def xfunc():
    global y  # HERE the global function changes the existing value in Y
    y = 5
    x = 1
    # y = "ONE"
    



    print(f"{x} is in local variable and is called out by function")

xfunc()
print(f"{x} is in global variable and is out of the function")
# print("here no 'y = ONE ' will be excecuted because its in LOCAL VARIABLE ")

print(f"The y = {y} is now used hook with the help of global keyword so it has become global variable")
