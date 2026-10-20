class person:  # Class namely person
    def __init__(self, n, o): # 3 conditions where SELF is PAPER or option slots which has name and occ itself
        self.name = n    # name is called by n 
        self.occ = o     # occupation called by o
        print("this is person")

    def info(self):      # self 
        print(f"{self.name} is a {self.occ}") 

a = person("Harry", "Developer")
b = person("rohan", "foodie")
a.info()
b.info()

class Car: # class is named car
    def __init__(self,horsepower): # 2 par's 
        self.horsepower = horsepower # self.horspower returns the option horsepower given on form

carA = Car("2500")  # Car(x) the Car here assigns the horsepower inside to be x 
carB = Car("2400")
print(f"the horsepower of carA is {carA.horsepower}")
print(f"the horsepower of carB is {carB.horsepower}")
'''
class SmartDevice:
    def __init__(self, deviceName, batteryPercentage):
        self.deviceName = deviceName
        self.batteryPercentage = batteryPercentage

myPhone = SmartDevice("iphone",85)
print(f"the battery percentage of {myPhone.deviceName} is {myPhone.batteryPercentage}")
'''

'''

class collegeAdmission:
    def __init__(self, course, year, studentName):
        self.studentName = studentName
        self.course = course
        self.year = year

webInput1 = input("Enter the course:\n")
webInput2 = input("Enter the year:\n")
webInput3 = input("Enter the student Name:\n")
collegeInfo = collegeAdmission(webInput1,webInput2,webInput3)
print(f"The Course of the student {collegeInfo.studentName} is {collegeInfo.course} which is in {collegeInfo.year}")

'''

class speciality:
    def __init__(self, name, skills, year):
        self.name = name
        self.skills = skills
        self.year = year

nameInput = input("Enter the Name of the player:\n")
skillsInput = input("Enter the skills of the player:\n")
yearInput = input("Enter the year in which player is:\n")

selectedPlayers = speciality(nameInput, skillsInput, yearInput)
print(f"the skill of the {nameInput} is {skillsInput} of {yearInput}")