# LAMBDA FUNCTION
'''used for one liner function and when function is used as argument'''

# def double(x):
#     return x*2         # This function will return its double but its lenghty and not efficient
# print(double(5))



# '''Lamda function simply takes x value and returns it with the given condition sitauted to it
#      lambda is a variable function and better than using def keyuword if there exist many 
#         functions in a single script'''
# double = lambda x: x*2
# x = int(input("enter the no!\n")) 
# print(f"double of {x} is {double(x)}")


# # MORE Ex by differianting def/ lambda:
# # 1
# def sum(x,y):
#  return x+y
# print(sum(5,5))
# 'OR'
# summ = lambda x, y: x+y
# print(sum(5,5)) 

# # 2
# def cube(x):
#    return x*x*x
# print(cube(2))
# 'OR'

cube = lambda x: x*x*x
print(cube(1))


# Passing the function to another function
def funcs(fs, value):
   return 1 + fs(value)
print(funcs(cube,3)) # cube goes to '1' and '3' goes to value
                     # cube of 1 is 1 and cube of 3 is 27 so 27+1 = 28

print(funcs(lambda x: x*x*x))
