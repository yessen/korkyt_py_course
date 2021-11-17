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


if __name__ == "__main__":
   Aik = Person()
   Aik.set_name('Aibek', 'Abeken')
   print(Aik.get_name())





   



