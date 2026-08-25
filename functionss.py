#Greeting function
'''def greetin(name):
    print(f"Hello {name}!")
    
name = input("Enter your name:? ")
   
greetin(name)
'''


#Addition function
'''
def addn(a, b):
    return a + b        
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))          
result = addn(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")     

addn(num1, num2)
'''

#find even number
'''
addn(a, b)

def is_even(num):
    if num % 2 == 0:
         print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")
num = int(input("Enter a number: "))
is_even(num)
'''

#greet multiple people with different religions
'''
def greet_multiples(names, religion):
    for name in names:
        if religion.lower() == "hindu":
            print(f"Namaste {name}")
        elif religion.lower()== "muslim":
            print(f"Assalamu Alaikum {name}")
        else:
            print(f"Hello {name}")

name = [n.strip() for n in input("Enter your names (separated by commas): ").split(",")]
religion = input("Enter your religion : ")


greet_multiples(name, religion)
'''
#greet people in different languages
'''
def greet_language(name, language):
    if language == 'english':
        print(f"Hello {name}!")
    elif language == 'hindi':
        print(f"Namaste {name}!")
    else:        
        print(f"Hello {name}! I don't know your language.")
name = input("Enter your name: ")
language = input("Enter your language (english/hindi): ").lower()
greet_language(name, language)
'''


#calculator function

'''
def calc(a, b, operation):
    if operation  == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation. Please choose +, -, *, or /."
    
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))   
operation = input("Enter the operation (+, -, *, /): ")
result = calc(a, b, operation)
print(f"The result of {a} {operation} {b} is: {result}")
'''


# finding max number
'''
def max_number(a):
    maax = a[0]

    for num in a:
        if num > maax:
            maax = num
    return maax

a = [int(x) for x in input("Enter a list of numbers separated by commas: ").split(',')]
print(f"The maximum number in the list is: {max_number(a)}")
'''

#counting vowels in a string
'''
def count_vowels(s):
    vowels  = 'aeiou'
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count
s = input("Enter a string: ")
print(f"The number of vowels in the string is: {count_vowels(s)}")

'''

#reversing a string
'''
def shinji_hikaro(s):
	return (s[::-1])
s = input("wanna invert something? \n")
"
print(f"your inverted shit is: {shinji_hikaro(s)}")
'''

#checking if a string is a palindrome


def ulta_ya_seedha(bs):
    return bs == bs[::-1]
    
bs = input("wanna check if it's a palindrome? \n")
if ulta_ya_seedha(bs):  
     print(f"{bs} is a palindrome.")
else:
      print(f"{bs} is not a palindrome.")
    
if __name__ == "__main__":
     ulta_ya_seedha()
# printing multiplication tables
'''
def tables(number):
	for multiples in range(1, 11):
		print(f"{number} * {multiples} = {number * multiples}")
	
number = int(input("Enter the number you want multiples of: "))
tables(number)
'''