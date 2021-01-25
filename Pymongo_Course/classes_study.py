class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def speak(self):
        print("users can speak")
        
    
    
        

# shamu = Person("Hello",12)
# shamu.welcome()

class Student(Person):
    
    def __init__(self,name,age,year):
        super().__init__(name,age)
        self.year = year
        self.actions = ["Attack","Defend"]
        
        
    def welcome(self):
        print("My name is ", self.name, "and age is ", self.age, "Year is ",self.year )
        
    
    
stu = Student("Shamu",24,2019)
stu.welcome()
stu.speak()
print(stu.actions)


