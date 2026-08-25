l= [10,15,5,20,25,35,20]

print(l.count(20)) #how many 20's are there in list
l.append(50) # adds the no 50 in the list
print(l)    
print(l.index(10)) # whats the index of no 10 in the list
print(l[0])    # what is the no on the index 0
l.sort(reverse=True) # reverses the list if its true 
print(l)
l.sort(reverse=False) # if its reversed then it will change to its normal condition
l.insert(0, 0) # insets the no 0 at 0
print(l)

newl = [100,150,200] 
l.extend(newl)  # changes the l list and adds the new data into it
print(l) 
# Or
k = l + newl # if we dont want to change the existing list then we can just add the two list
print(k)