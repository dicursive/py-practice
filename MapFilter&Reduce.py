'''
LAWS of map, filter and reduce

1. map(function, iterable) returns whatever the function returns for each element.

2. filter(function, iterable) expects the function to return something that can be interpreted as True or False.
    If the function returns True, the original element is kept.
    If it returns False, the original element is discarded.

3. Reduce(function, iterable) reduces the given list to a single output according to the condition
'''



# MAP
'''
def cube(x):
    return x*x*x

l = [1,2,4,5,6]
print(f"the list is {l}")
newl = []

#we create a newl file which stores the upcoming value by appending in it

for item in l:
    newl.append(cube(item)) # in a blank list, add each items cube individually

print(newl)

newl = list(map(cube, l))
print(newl)
'''


#With help of lambda
'''
newll = list(map(lambda x: x/2, l))
print(newll)
'''

# Filter function
'''
def filtereg(a):
    return a>2
newlll = list(filter(filtereg, l))
print(f"list given by filter function is {newlll}")

newl = list(map(filtereg,l))
print(newl)
'''
#Reduce Function 
'''
from functools import reduce
listsum = [1,2,3,4]
def summin(x,y):
    return  x + y
sumlist = reduce(summin, listsum)
print(sumlist)
'''


# def cube(x):
#     return x*x*x

# l = [1,2,4,5,6]
# print(f"the list is {l}")
# newl = []

# #we create a newl file which stores the upcoming value by appending in it

# #for item in l:
#  #   newl.append(cube(item)) # in a blank list, add each items cube individually

# # print(newl)

# newl = list(map(cube, l))
# print(newl)

'''
# MAPPing function
def subList(inpt, numbbers):
    return inpt - numbbers

inpt = int(input("Enter yo number:\n"))
no = [19,23,53,123]

newNo = []

for numberr in no:
    newNo.append(subList(inpt,numberr))

print(newNo)

# by map function 
newLI= []

newLI = list(map(lambda noX : subList(inpt, noX), no))#the noX here is iterable variable name giving value as for loop
#       list(map(lambda iterable name: functions name (input, iterable name), the source of list))
print(newLI)   '''                     


# Filter Function
'''
no = [19,23,53,123]
def filterqn(innput, givenList):
    return givenList > innput

innput = int(input("Enter the no"))

result = list(filter(lambda x : filterqn(innput, x), no))
print(result)
'''

# Reduce Function with function
no = [10,20,30,40,50]
from functools import reduce
def mltply(x,y):
    return x*y
nm = reduce(mltply,no)
print(nm)

# Reduce function with lambda or one liner function 
nm = reduce(lambda frst,scnd: mltply(frst, scnd), no)
print(nm)

# mn = list(reduce(mltply,no))
# print(mn)