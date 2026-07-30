class Student:

    def __init__(self,name):
        self.name = name 

    def study(self):

        print(self.name, "is studying")

student = Student("John")
student.study()