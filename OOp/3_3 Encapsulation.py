### Public Access Modifier
##  Public
class Person_03:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  
  def display_03(self):
    print(f"The name is {self.name} and the age is {self.age}")

person_03 = Person_03("Md", 27)
person_03.display_03()
