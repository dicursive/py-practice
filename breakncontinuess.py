# Break statement in for and while loop
'''The break statment ends the loop

for i in range(1,10):
    i = i +1
    print(i)
    if i == 10:
       
        break
'''


# continue statemnt skips the iteration
'''
i = 0
while(i<= 10):
    i = i+1 
    
    if i %2 == 0:
        print("'skippsssss the iterations' ")
        continue
    print(i)
'''

# Emulating the DO while loop
'''it runs the code for atleast one time irrespective if the condition is true or not'''

i = 0
while True:
    i = i+1 
    
    if i %10 == 0:
        break
    print(i)
