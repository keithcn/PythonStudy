class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print("dog "+self.name+" is sitting now.")



mydog = Dog("keith",23)
mydog.sit()

mydog.name = "hao"
mydog.sit()