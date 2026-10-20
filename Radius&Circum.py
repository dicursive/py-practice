# Circle
# radius = float(input("Enter the radius\n:"))
# area = 3.14*radius**2
# print(area) 
# circum = 2*3.14*radius
# print(circum)

# # Rectangle
# ln = float(input("enter the length of rectangle"))
# br  = float(input("enter the breadth of rectangle"))
# print(f"{ln} is ln")
# print(f"{br} is br")
# area = ln*br
# print(f"{area} of rectangle")
# circum = 2*(ln+br)
# print(circum)

# temp = ln   
# ln = br
# br = temp
# print(f"{temp} is ln")
# print(f"{ln} is br")


#fibonacci series
n = int(input("enter the number\n"))
f0 = 0
f1 = 1
if (n<0):
    print("input bigger then 0")
else:
    print(f"fibonacci series of {n} terms is")
    print(f0)
    print(f1)
    for i in range(2,n):
        f= f0+f1
        print(f)
        f0 = f1
        f1 = f
        