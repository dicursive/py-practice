# Match Case Statement

x = int(input("enter the no: \n"))

match x:
    case 0:
        print(f"x is {x}")
    case 4:
        print(f"x is {x}")
    case _ if x!= 90:
        print(f"x is {x}")
    case _ if x== 100:
        print(f"x is {x}")
    case _ :            #default case
        print(x)