# class person:  # Class namely person
#     def __init__(self, n, o): # three conditions
#         self.name = n    # name is called by n
#         self.occ = o     # occupation called by o
#         print("this is person")

#     def info(self):      # self 
#         print(f"{self.name} is a {self.occ}")

# a = person("Harry", "Developer")
# b = person("rohan", "foodie")
# a.info()
# b.info()

class Car:
    def __init__(self,horsepower):
        self.horsepower = horsepower

carA = Car("2500")
carB = Car("2400")
print(f"the horsepower of carA is {carA.horsepower}")
print(f"the horsepower of carB is {carB.horsepower}")