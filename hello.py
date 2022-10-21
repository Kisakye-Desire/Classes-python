class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"The name is {self.name} and the age is {self.age}"
        
#person1 = Person('John', 20)
#person2 = Person('Desire', 30)

#print(person1)
 #print(Person2)





class Student(Person):
    def __init__(self,name,age,access_no,program):
        super().__init__(name,age)
        self.access_no = access_no
        self.program = program
        
        
    #Method for adding behaviour to function.
    def start_walking(self):
        print(f"{self.name} is walking........💃💃💃")
    
    def __str__(self):
        return f"The name is{self.name}  and the age is{self.age}"
student1 = Student('Desire',20,'A92401','BSIT')

#Print to the terminal
print(student1)

#Printing the method of start_walking (Call the object and the method name)
student1.start_walking()

