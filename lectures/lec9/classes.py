class Person():
   age = 0
   rost = 0
   name = ''
   lastname = ''

   # Constructor
   def __init__(self, init_name = "Aibek", \
                      init_lastname = "Abeken", \
                      init_age = 20, \
                      init_rost = 170):
     self.name = init_name
     self.lastname = init_lastname
     self.age = init_age
     self.rost = init_rost
 
     print("Vse attributy initsializirovany!!!")

   # Getter methods
   def get_name(self):
     return (self.name, self.lastname)
   
   def get_age(self):
     return self.age

   def get_rost(self):
     return self.rost

   # Setter methods
   def set_name(self, new_name, new_lastname):
       self.name = new_name
       self.lastname = new_lastname

   def set_age(self, new_age):
       self.age = new_age

   def set_rost(self, new_rost):
       self.rost = new_rost

   # Print Person info in format:
   #    Name: name lastname
   #    Age: age
   #    Rost: rost
   def print_info(self):
       print("Name:", self.name, self.lastname)
       print("Age:", self.age)
       print("Rost:", self.rost)
       # print attr1
       # print attr2 


# Student class
class Student(Person):
  # 1 nemese 2 attribut kosu kerek
  #
  # jana attributtrga getter/setter metodtar jasau
  # init, print_info - ozgeris jasau kerek
  # def print_info():
  #    ..... + jana attributtardy da shygaru kerek


  # Constructor
  def __init__(self, init_name = "Aibek", \
                      init_lastname = "Abeken", \
                      init_age = 20, \
                      init_rost = 170, \
                      init_attr1 = "bir man attr1", \
                      init_attr2 = "bir man attr2"):
        super().__init__(init_name, init_lastname, init_age, init_rost)
        self.attr1 = init_attr1 
        self.attr2 = init_attr2 

   # Print Student info in format:
   #    Name: name lastname
   #    Age: age
   #    Rost: rost
   #    Attr1: attr1
   #    Attr2: attr2
   def print_info(self):
       print("Name:", self.name, self.lastname)
       print("Age:", self.age)
       print("Rost:", self.rost)
       # print attr1
       # print attr2 

# Teacher class

class Teacher(Person):
  # 1 nemese 2 attribut kosu kerek
  #
  # jana attributtrga getter/setter metodtar jasau
  # init, print_info - ozgeris jasau kerek
  # init-ta Person-nin jane Studenttin manderin berip
  # super() arkyly  Person-nin manderin initsializatsiya jasau
  # def print_info():
  #    ..... + jana attributtardy da shygaru kerek

  # Constructor
  def __init__(self, init_name = "Aibek", \
                      init_lastname = "Abeken", \
                      init_age = 20, \
                      init_rost = 170, \
                      init_attr1 = "bir man attr1", \
                      init_attr2 = "bir man attr2"):
        super().__init__(init_name, init_lastname, init_age, init_rost)
        self.attr1 = init_attr1 
        self.attr2 = init_attr2 
 
if __name__ == "__main__":
   Aik = Person()

   # Adamnin atyn ozgertu
   Aik.set_name("Sultan", "Taspenov")
   Aik.set_age(25)
   

   Aik.print_info()

   stud = Student()
   stud.print_info()
   #print(stud.attr1)
   #print(stud.attr2)
    


   



