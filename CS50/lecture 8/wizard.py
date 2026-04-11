#Inheritance allows us to inherit the atrributes of the superclass , here wizard is the superclass 

class Wizard:
    
    def __init__(self, name):

        if not name :

            raise ValueError("Missing name")
        self.name = name 


class Student(Wizard):

    def __init__(self, name , house):

        super().__init__(name) #super() is used to call the constructor of the superclass and initialize the name attribute
        self.house = house

class Professor(Wizard):

    def __init__(self, name, subject):
        
        super().__init__(name)
        self.subject = subject


wizard = Wizard("Albus Dumbledore")
student = Student("Harry Potter", "Gryffindor")
professor = Professor("Severus Snape", "Defense Against the Dark Arts")