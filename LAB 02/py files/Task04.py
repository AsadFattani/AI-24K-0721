class Employee:
    def work(self):
        print("Employee is working.")

class Manager(Employee):
    def work(self):
        print("Manager is managing.")

class Developer(Employee):
    def work(self):
        print("Developer is developing.")

class Designer(Employee):
    def work(self):
        print("Designer is designing.")

e1 = Manager()
e1.work()
e1 = Developer()
e1.work()
e1 = Designer()
e1.work()