
Classes are created by keyword class.
Attributes are the variables that belong to a class.
Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute
Creating an Object
  
  obj = Dog()

The Python self  
  Class methods must have an extra first parameter in the method definition. We do not give a value for this parameter when we call the method, Python provides it
  If we have a method that takes no arguments, then we still have to have one argument.
  This is similar to this pointer in C++ and this reference in Java.

  When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) – this is all the special self is about.

The __init__ method is similar to constructors in C++ and Java. It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.

