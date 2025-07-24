### Access Modifier ---> Encapsulation
##  Protected
class Person_02:
  def __init__(self, name, age):
    self._name = name
    self._age = age

  
  def display_02(self):
    print(f"The name is {self._name} and the age is {self._age}")


class Student(Person_02):
  def __init__(self, name, age):
    super().__init__(name, age)

  def display_02(self):
    print(f"The name is {self._name} and the age is {self._age}")


student_01 = Student("Md", 27)
student_01.display_02()
