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
#  index is the number and n is the looping place of the thing in list
    print(n)    
    if index == 3:
        print(f"number is {numbers[index]}")


# print by index number

numbers = [10,20,30,40]

for index,n in enumerate(numbers, start= 1):
    print(index, n)

guests = ["Alice", "Bob", "Charlie", "Diana"]

for table,visitors in enumerate(guests,start=1):
     print(f"table {table} for {visitors}") 


#remove blank spaces

skills = [" Python ", "JavaScript", "  SQL", "HTML "]
for blankspace,present in enumerate(skills):
    skills[blankspace] = present.strip()
    print(skills)


#Printing even no coz odd is corrupted

passwords = ["safe123", "CORRUPT_pw", "mySecret99", "BAD_PASS", "pythonic42"]
for evenNo,pas in enumerate(passwords):
   if evenNo % 2 == 0:  # This covers 0, 2, and 4
        print(f"Index {evenNo} is safe: {pas}")

        

#check the market
prices = [100, 105, 102, 98, 104, 101]
for days,pattern in enumerate(prices):
    if pattern == 100:
        continue
    if prices[days-1] > pattern:
        print(f"Day {days}: Price dropped to {pattern}")