class Car:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
    def display(self):
        print(f"model {self.model} brand {self.brand}")
car1=Car("BMW","Lamborgini")
car1.display()