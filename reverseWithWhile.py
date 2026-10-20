num = int(input("Enter the integer number"))
rev_num = 0
while(num > 0):
   # The main logic is below
   remainder = num % 10 
   # remainder will give the last digit of every num
   rev_num = (rev_num * 10) + remainder
   # at first rev_num is just remainder
   num = num//10
   # num// reduces the last digit
   # then the num moves back again to start loop again until the value is 0
   

print(f"the reverse number is {rev_num}")