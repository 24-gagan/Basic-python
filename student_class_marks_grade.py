class Students:
    def __init__(self,marks,name):
        self.name=name
        self.marks=marks
    def calculate_grade(self):
        if self.marks==90:
            print("Your grade is A")
        elif self.marks==70:
            print("Your grade is B")
        elif self.marks==60:
            print("Your grade is C")
        else:
            print("grade D")
    def display(self):
        grade=self.calculate_grade()
        print(f"Your name is {self.name}")
        print(f"Your marks are {self.marks}")
        print(f"Your grade is {grade}")
s1=Students("Gagan",70)
s1.display()