# n = int(input("enter no"))
# f0 = 0
# f1 = 1
# if (n<0):
#     print(f"enter bigger number than{n} ")
# else:
#     # print(f0)
#     # print(f1)
#     for i in range(2,n):
#         f = f0 + f1
#         print(f)
#         f0 = f1
#         f1 = f

#reversing a string
# num = int(input("enter the integer number\n:"))
# revNum = 0 
# while(num>0):
#     remainder = num % 10
#     revNum = (revNum *10) + remainder
#     num = num//10
# print(revNum)

num = int(input("enter the integer number\n:"))
oldNo = num
revNum = 0 
while(num>0):
    remainder = num % 10
    revNum = (revNum *10) + remainder
    num = num//10

if (oldNo == revNum):
    print(f"{oldNo} is palindrome")
else:
    print("not a palindrome")


