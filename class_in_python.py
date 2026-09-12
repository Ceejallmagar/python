class Dog:
    species="canis lupus"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def bark(self):
        return f"dog {self.name} barked"


dog1=Dog("upe",12)

print(dog1.bark())