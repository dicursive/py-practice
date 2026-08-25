# #   S(0)  W(1)   G(2)
# #S   D      W      L
# #W   L      D      W
# #G   W      L      D

# import random

# options = [0, 1, 2]
# name = ['snake', 'water', 'gun']

# cmptrpnt = 0
# userpnt = 0
# user_name = input("Enter your name:\n")
# i = 0

# while i <= 9:
#      i = i + 1
#      print(f"Round {i}\n")
#      print("Note: Choose 0 for snake, 1 for water and 2 for gun")

#      rndmNo = random.choice(options)
#      print(f"COMPUTER CHOOSES: {name[rndmNo]}={rndmNo}")
#      userInput = int(input("Your choice?:"))
#      if i == 10:
#         if userpnt>cmptrpnt:
#                  print(f"{user_name} wins with {userpnt} points.")
#         elif cmptrpnt>userpnt:
#                  print(f"Computer wins {cmptrpnt} points.")
#         else:
#            print(f"The match is draw with\n{user_name}:{userpnt} points | Computer:{cmptrpnt} points")
        
#     elif userInput == rndmNo:
#         print(f"Computer gets:{cmptrpnt} points  {user_name} gets:{userpnt} points")
#         print("The match is draw")
#     elif userInput == 0 and rndmNo == 1:
#         userpnt += 1
#         print(f"{user_name} wins \n snake drank the water ")
#         print(f"{user_name} gets {userpnt} and computer gets {cmptrpnt}")
#     elif userInput == 1 and rndmNo == 0:
#         cmptrpnt += 1
#         print(f"Computer wins \n snake drank the water ")
#         print(f"Computer gets {cmptrpnt} and {user_name} gets {userpnt}")
#     elif userInput == 1 and rndmNo == 2:
#         userpnt += 1
#         print(f"{user_name} wins.\nGun drown in water.")
#         print(f"{user_name} gets {userpnt} and computer gets  {cmptrpnt}")
#     elif userInput == 2 and rndmNo == 1:
#         cmptrpnt += 1
#         print(f"Computer wins.\nGun drown in water.")
#         print(f"Computer gets {cmptrpnt} and {user_name} gets {userpnt}")
#     elif userInput == 0 and rndmNo == 2:
#         cmptrpnt += 1
#         print(f"Computer wins.\nGun shot the snake.")
#         print(f"Computer gets {cmptrpnt} and {user_name} gets {userpnt}")
#     elif userInput == 2 and rndmNo == 0:
#         userpnt += 1
#         print(f"{user_name} wins.\nGun shot the snake.")
#         print(f"{user_name} gets {userpnt} and computer gets {cmptrpnt}")
   
#     else:
#         print("Wrong input. Try again!")


import random

options = [0, 1, 2]
name = ['snake', 'water', 'gun']

cmptrpnt = 0
userpnt = 0
user_name = input("Enter your name:\n")
i = 0

while i<=10:
    i = i + 1
    print(f"\n\nRound {i}\n")
    print("Note: Choose 0 for snake, 1 for water and 2 for gun")

    rndmNo = random.choice(options)
    print(f"COMPUTER CHOOSES: {name[rndmNo]}={rndmNo}")
    userInput = int(input("Your choice?:"))
    if userInput == rndmNo:
            print("match is darw")
    elif (userInput - rndmNo) % 3 == 2:
            print(f"{user_name} wins")
    elif i == 10:       
        if userpnt>cmptrpnt:
                 print(f"{user_name} wins with {userpnt} points.")
        elif cmptrpnt>userpnt:
                 print(f"Computer wins {cmptrpnt} points.")
        else:
             print("The match was draw")
    else:
       print("computer wins") 







#gng why my real homies or like the people i loved goes far away?like im a guy who looks tuff when im not friend like im all silent, no eye contact, less talk guy but when someone tried to be my friend or like im starting to be friend with them thenn i become kind of wierdo who 