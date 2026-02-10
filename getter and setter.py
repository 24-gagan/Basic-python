class Employee:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name
    def get_salary(self):
        return self.__salary
    def set_salary(self,salary):
        if salary>0:
            self.__salary=salary
        else:
            print("invalid salary")
s1=Employee("gagan",100000)
print(s1.get_name())
print(s1.get_salary())

# Using setters
s1.set_name("Amit")
s1.set_salary(60000)

print(s1.get_name())
print(s1.get_salary())