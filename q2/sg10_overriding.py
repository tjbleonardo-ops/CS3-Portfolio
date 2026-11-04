#creates animal parent class
class Animal():
  def __init__(self,name):
    self.__name = name
    
#inheritable method eat 
  def eat(self, name, type):
    if type == "lion": 
      return f"{name} eats fresh meat."
    elif type == "elephant": 
      return f"{name} eats grass and fruits."
    elif type == "monkey": 
      return f"{name} eats bananas."
#inheritable method make sound
  def make_sound(self, name, type):
    if type == "lion": 
      return f"{name} roars loudly!"
    elif type == "elephant": 
      return f"{name} trumpets!"
    elif type == "monkey": 
      return f"{name} chatters!"
#child class lion
class Lion(Animal):
  def __init__(self, name):
    super().__init__(name)
    self.__name = name
#calls inherited methods    
  def eat(self):
    return super().eat(self.__name,"lion")

  def make_sound(self):
    return super().make_sound(self.__name,"lion")
#child class elephant
class Elephant(Animal):
  def __init__(self, name):
    super().__init__(name)
    self.__name = name
#calls inherited methods       
  def eat(self):
    return super().eat(self.__name,"elephant")

  def make_sound(self):
    return super().make_sound(self.__name,"elephant")
#child class monkey    
class Monkey(Animal):
  def __init__(self, name):
    super().__init__(name)
    self.__name = name
#child class elephant    
  def eat(self):
    return super().eat(self.__name,"monkey")

  def make_sound(self):
    return super().make_sound(self.__name,"monkey")
#prints output
l1 = Lion("Simba")
e1 = Elephant("Dumbo")
m1 = Monkey("George")
animal_list = [l1,e1,m1]
for i in animal_list:
  print(i.make_sound())
  print(i.eat())
  print("-------")
