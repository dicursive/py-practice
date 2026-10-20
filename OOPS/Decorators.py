# ============================================================
# DECORATORS IN PYTHON
# ============================================================


# ------------------------------------------------------------
# 1. Basic Decorator
# ------------------------------------------------------------
'''DECORATORS modifies the function and returns'''

# def decoratorEg(fx):           # The 'fx' is the function which decorators takes as input to modify
#     def modifying_function():  # The function or say 'fx'  is being the argument
#         print("first function")#         } before function
#         fx()                   # <-syntax} the function
#         print("functions out") #         } out of the function
#     return modifying_function  # the function doing its work

# @decoratorEg    # The Decorator will be called here and do it jobs
# def sayHello(): # The 'sayHello' is 'fx' 
#     print("helloji sanam")
# sayHello()




# ------------------------------------------------------------
# 2. Decorator with *args
# ------------------------------------------------------------
'''taking values for argumnt from funct i.e fx inside a decorator, use *args- (means tuple) & **kwargs-(dictionary)'''
# def decorator2(fxx): 
#     def modified2(*args):
#         print("second function")
#         fxx(*args)
#         print("function ends here")
        
#     return modified2

# @decorator2
# def sum(a,b):
#     return a+b
# x = int(input("enter no1\n:"))
# y = int(input("enter no2\n:"))
# c= sum(x,y)
# print(c)

# def decorator2(fxx):
#   def modified2(*args):
#     print("second function")  # Added quotes
#     result = fxx(*args)  # Capture the returned sum
#     print("function ends here")  # Added quotes
#     return result  # Return the sum to the caller
#   return modified2


# @decorator2
# def sum(a, b):
#   return a + b

# x = int(input("enter no1\n: "))
# y = int(input("enter no2\n: "))
# c = sum(x, y)
# print(c)

# ------------------------------------------------------------
# 3. Decorator for Error Handling / Retrying
# ------------------------------------------------------------

# import random
# times = 4
# # 1. Triple-layered decorator to accept arguments
# def retry(times):
#     def decorator(fx):
#         def wrapper(*args, **kwargs):
#             for attempt in range(times):
#                 try:
#                     return fx(*args, **kwargs)
#                 except:
#                     Exception 
                
               
#         return wrapper
#     return decorator

# # 2. A simulated flaky function to test your decorator
# @retry
# def unstable_network_call():
#     print("Attempting to connect to server...")
#     if random.choice([True, False]): # 50% chance to fail
#         raise ConnectionError("Server timed out!")
#     return "Success: Data fetched!"

# # 3. Test it out
# try:
#     result = unstable_network_call()
#     print(f"\nFinal Result: {result}")
# except ConnectionError as e:
#     print(f"\nFinal Result: Permanent Failure! Error: {e}")




# # 1. Triple-layered decorator to accept arguments
# import random
# def retry(times):
#     def decorator(fx):
#         def wrapper(*args, **kwargs):
#             # We use a loop to keep track of remaining attempts
#             for attempt in range(times):
#                 try:
#                     # Try to run the function. If it works, return the result immediately!
#                     return fx(*args, **kwargs)
                
#                 except ConnectionError as e:
#                     # If fx() crashes with a ConnectionError, Python jumps straight here!
#                     remaining_attempts = times - (attempt + 1)
#                     print(f"Function failed! Remaining attempts: {remaining_attempts}")
                    
#                     # If we have no attempts left, we finally let the error crash the program
#                     if remaining_attempts == 0:
#                         print("No attempts left!")
#                         raise e
                        
#         return wrapper
#     return decorator

# # 2. Applying the decorator with the argument (times=4)
# @retry(times=4)
# def unstable_network_call():
#     print("Attempting to connect to server...")
#     if random.choice([True, False]): # 50% chance to fail
#         raise ConnectionError("Server timed out!")
#     return "Success: Data fetched!"

# # 3. Test it out
# try:
#     result = unstable_network_call()
#     print(f"\nFinal Result: {result}")
# except ConnectionError as e:
#     print(f"\nFinal Result: Permanent Failure! Error: {e}")


#_________________________________________________________________________
# using for loop in decorators
#-------------------------------------------------------------------------

# # 1.The outer doll:Layer1 The Boss: Only cares about the settings. It grabs num_times=3 and hands it down.
# def repeat(num_times):
# # 2.The middle doll:Layer2 The Manager: Only cares about the target.It grabs shout function and hands it down.
#     def decorator(fx):
# # 3.The inner doll:Layer3 The Worker: Has access to everything now.It knows it needs to run shout (from Layer 2) exactly 3 times (from Layer 1).
#         def wrapper(*args, **kwargs):
#             for rounds in range(num_times):
#                 fx(*args, **kwargs)  # 🚨 FIX: Removed 'return' from here so it loops!
#         return wrapper  # Returns the inner doll to the middle doll
#     return decorator  # Returns the middle doll to Python

            
            

# # 2. Apply it here
# @repeat(num_times=3)
# def shout():
#     print("Hurrah!")

# # 3. Test it
# shout()


#___________________________________________________________________
# QUIZES
#-------------------------------------------------------------------

#🟢 Level 1: The Gatekeeper (2 Layers)
'''prints the square of positive numbers and returns error if negative'''
def positiveOnly(square):
    def numberChecker(*args,**kwargs):
        square(*args,**kwargs)
    return numberChecker

@positiveOnly
def square(num):
    if num>0:
        print(num*num)
    else:
        print("error!! number is smaller than 0")
num = int(input("enter the num\n:"))   
square(num)


#🟡 Level 2: The Multiplier (3 Layers)
'''multiplies the factor values to the function 'add'  '''

def multiplyResult(factor):
    def grabber(addd):
        def main(*args, **kwargs):
            result = addd(*args, **kwargs) 
            return result * factor
        return main
    return grabber

@multiplyResult(factor=10)
def addd(a, b):
    return a + b
a = int(input("enter no:\n"))
b = int(input("enter no:\n"))

c= addd(a, b)# (2+3) is 5. 5 * 10 should print 50!
print(c)


#🟠 Level 3: The Secret Agent (3 Layers)
'''Create a 3-layered decorator called @mask_string(char="*")'''

def maskString(char):
    def manager(getCreditCard):
        def security(*args, **kwargs):
            result = getCreditCard(*args, **kwargs)
            s1 = (result[:-4])
            s2 = (result[-4:])
            s3 = (len(s1))
            s4 = s3 * char
            return s4+s2
    # or just do 
    # return (char * len(result[:-4])) + result[-4:]

        return security
    return manager
            
@maskString(char="#")
def getCreditCard():
    return "1234567890123456"

print(getCreditCard()) # Should print ############3456



#🔴 Level 4: Boss Mode — The Delay Timer (3 Layers)
'''Create a 3-layered decorator called @delay(seconds).'''
import time
def delay(seconds):
    def middleMan(sayHi):
        def delayer(*args, **kwargs):
            time.sleep(seconds)
            sayHi(*args,**kwargs)
        return delayer
    return middleMan



@delay(seconds=2)
def sayHi():
    print("Hello after 2 seconds!")

sayHi() # There should be a visible 2-second pause in your terminal before "Hello..." prints