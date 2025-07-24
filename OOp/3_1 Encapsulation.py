### Access Modifier ---> Encapsulation
##  Private
class Person_01:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age

  
  def display(self):
    print(f"The name is {self.__name} and the age is {self.__age}")


person_01 = Person_01("Md", 27)
person_01.display()
