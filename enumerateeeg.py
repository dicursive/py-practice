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