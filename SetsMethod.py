# Sets contains all types of values and it returns only one value if two same are present
# The order is not maintained in the set

# example
s = {1,1.5,False, "Sets", "0", 1.5} 
print(s)

 
emptySet = set() 
# to create an empty set

print(type(emptySet)) 
# Output is class<Set>

x = {}
print(type(x)) 
# this will return class<dict>

for values in s:
    print(values) 
    # the order of values will not be maintained
    