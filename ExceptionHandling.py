
# Try and Except




# 1
try:
    age = int(input("Enter your age?: \n"))
    print(f"your age is {age}")
    
except :
    print("some error ocurred")


# 2

def divide(num1, num2):
    try:
        print(f"{num1} / {num2} is ", num1 / num2 ) 
    except:
        print("not divisible by 0")

num1 = int(input("enter the first number:\n"))
num2 = int(input("enter the second number:\n"))

divide(num1, num2)
    
# 3


mixed_data = [10, "hello", 20, "world", 30]

for item in mixed_data:
    try:
        result = int(item) * 2 
        print(f"Result is: {result}")

    except:
        print("Invalid typo")




# 4

def check_values(x, y):
    try:
        result = int(x) +  int(y)
        print(result)
    except:
        print("Error: Mixed types!")
 
x = input("enter the first number:\n")
y = input("enter the second number:\n")

check_values(x, y)


# 5 
fruits = ["apple", "banana", "cherry"]

index = [0, 2, 5, 1]


for i in index:
    try:
        print(fruits[i])

    except:
        print(f"The index no {i} doesnt exists in the list of fruit")
