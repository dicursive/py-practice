# using finally function
'''The finally function runs irrespectively and its used in functions, closing the files, datasets'''







def funct():
    try:
        print(fruits[index])

    except:
        print(f"The index no {index} doesnt exists in the list of fruit")

    finally:
        print(f"fruits are goood for haelth!")

index = int(input("Enter the index no"))
fruits = ["Apple", "Banana", "Cherry"]
funct()