# 1} '==' Compares the Values
# 2} 'is' Exact location of object in memory or Compares IDENTITY
#   The TRUE or FALSE output varies depending on mutability (changeable or unchangeable)
#  values in list can be changed by adding,removing,appending so python creates 2 distinct memory location for list
# tuples cant be changed so therfore they can result TRUE 


'''
a = [1,2,43]
b = [1,2,43]
print(a is b) # (FALSE) because list is 
print(a == b) # (TRUE) because values are same 
'''


x = (1,2,43)
y = (1,2,43)
print(x is y)
print(x == y)

z = [1,2,43]
b = [1,2,43]
print(z is b)
print(z == b)
