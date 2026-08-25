# READLINES

# file1 = open("file1(for readline).txt", "r")
# name = ['ram', 'rehman', 'anthony']
# subject = ['physics', 'chemistry','maths']
# l = 0
# while True:
#     l = l + 1
#     line = file1.readline().strip()
#     if not line:
#         break
    
#     l1 = line.split(",")[0]
#     l2 = line.split(",")[1]
#     l3 = line.split(",")[2]
#     print(f"the marks of '{name[0]}' in subject '{subject[0]}' is '{l1}'")
#     print(f"the marks of '{name[1]}' in subject '{subject[1]}' is '{l2}'")
#     print(f"the marks of '{name[2]}' in subject '{subject[2]}' is '{l3}'\n")

#WRITELINES

file2 = open("file1(for readline).txt", "a") # using this file for writing in it this time
lines = ['line1\n', 'line2\n', 'line3\n']
file2.writelines(lines)
file2.close