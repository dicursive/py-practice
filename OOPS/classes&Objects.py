class student: # Class is like a modle of form and we fill the information in it
    name = "rohan"
    standard = "second year"
    course = "B.Tech"
    duration = "4 years"
    def info(self): # 
        print(f"{self.name} is enrolled in course {self.course}\n is in {self.standard} with duration of {self.duration}              ")



# Below info will replace the values of above
a = student
a.name = "farhan"
a.standard = "first year"
a.course = "B.com"
a.duration = "3 years"
a.info(a)

# the variables and all can be changed or even many variables can be placed
b = student
b.name = "rehan"
b.standard = "third year"
b.course = "B.E"
b.duration = "4 years"
b.info(b)