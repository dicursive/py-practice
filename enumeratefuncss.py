# Enumerate Functions

numbers = [13,443,56,76]

'''for n in numbers:
    print(n)
    if numbers[3] == n:
        print(f"Number is {numbers[3]}")
'''

# we can manually make the index come down to any number we want'''


'''
index = 0
for n in numbers:
    print(n)
    if index == 3:
        print(f"Number is {numbers[3]}")
    index = index + 1
'''

# Enumerate function lets us do that simpplyy'''

for index, n in enumerate(numbers,start= 1): #the start is optional and it starts th index with the option provided to it

    print(n)
    if index == 3:
        print(f"number is {numbers[index]}")