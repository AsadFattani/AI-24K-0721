class Student:
    def __init__(self, name, grade):
        self.__name = name 
        self.__grade = grade

    def get_name(self):
        return self.__name
    
    def get_grade(self):
        return self.__grade
    
    def set_grade(self, grade):
        self.__grade = grade

    def display(self):
        print(f"Name: {self.__name}, Grade: {self.__grade}")

s = Student("Alice", "A")
s.display()
s.set_grade("A+")
print(s.get_grade())



