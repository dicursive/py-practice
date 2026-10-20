def argsnkwargs(*numbers, **kwargs):# *args takes input as tuple  kwargs takes inputs as dictionary 
    sum = 0               
    for i in numbers:    #'i' changes its place as per number or argument(whatever much) given
        sum = sum + i    #'sum' takes the value of 'i' and in another round it adds the value of 'i' to become sum
    print(f" {sum} ")    #'sum' is total summations of all inputs or number given 
argsnkwargs(5,10,20)     #the value of numbers were given in this line 
    