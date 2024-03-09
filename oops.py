class Myclass:
    def __init__(self) -> None:
        self.public_var = 10  # Public variable
        self._protected_var = 20  # Protected variable
        self.__private_var = 30  # Private variable 

    def get_private_var(self):
        return self.__private_var    


class Mysubclass(Myclass):
    def __init__(self) -> None:
        super().__init__()
        print("protected variable in child class", self._protected_var)


#create an instance of sub class  Y9t4f/shetappu@18

sub=Mysubclass()     
private=sub.get_private_var()
print(private)           



# create an inheritance

class person:
    def __init__(self, name, idnumber) -> None:
        self.name=name
        self.idnumber=idnumber

    def details(self):
        print(f"My name is {self.name}")
        print(f"My idnumber  is {self.idnumber}")  

class Employee(person):
    def __init__(self,name,idnumber,post, city):
        self.city = city
        self.post = post
        print("before")
 
        # invoking the __init__ of the parent class
        person.__init__(self, name, idnumber)  
        print("After")

    def details(self):
        print(f"My name is {self.name}")
        print(f"My idnumber  is {self.idnumber}")     
        print(f"My post  is {self.post}")   

Emp=Employee("rahul",500, "techie", "kenya" )        
Emp.details()









