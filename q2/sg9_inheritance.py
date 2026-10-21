#creates the class
class Publication:
  def __init__(self, title, author): 
    self.__title = title
    self.__author = author
 #methods 
  @property
  def get_title(self): 
    return self.__title
    
  @property
  def get_author(self):
    return self.__author

  def set_title(self, title):
    self.__title = title

  def set_author(self, author):
    self.__author = author
  @property  
  def display_info(self): #displays the title and author
    print(f"Title: {self.__title}")
    print(f"Author: {self.__author}")

class Book(Publication):
  def __init__(self, title, author, number_of_pages):
    super().__init__(title, author) #inherits from parent class Publication
    self.__number_of_pages = number_of_pages
  
  def get_number_of_pages(self):
    return f"Number of pages: {self.__number_of_pages}"

  def set_number_of_pages(self, number_of_pages): 
    if number_of_pages < 0:
      print("Number of pages must be positive.") #validates data, if the value is negative it doesn't change
    else:
      self.__number_of_pages = number_of_pages 
      
class Magazine(Publication):
  def __init__(self, title, author, issue_number):
    super().__init__(title, author) #inherits from parent class Publication
    self.__issue_number = issue_number
  
  def get_issue_number(self):
    return f"Issue Number: {self.__issue_number}"

  def set_issue_number(self, issue_number):
    if issue_number < 0:
      print("Issue number must be positive.") #validates data, if the value is negative it doesn't change
    else:
      self.__issue_number = issue_number
#object constructors
pub1 = Publication("The Effects of Sleep Deprivation on Item and Associative Recognition Memory","Ratcliff, R., & Van Dongen")
pub2 = Publication("What Do Undergraduates Learn About Human Intelligence?","Warne, R. T., Astle, M. C., & Hill, J. C.")
book1 = Book("The Metamorphosis","Franz Kafka",70)
book2 = Book("The Art of War","Sun Tzu",100)
mag1 = Magazine("The Wonders of The World","Corporal Navi",134)
mag2 = Magazine("Hello World","Pie Thon",45)
#displays all publication
print("Publication Information:") 
pub1.display_info                   
pub2.display_info
#diplays all books
print("\nBook Information:")
book1.set_number_of_pages(-60)
book1.display_info
print(book1.get_number_of_pages()+"\n")

book2.display_info
print(book2.get_number_of_pages())
#displays all magazines
print("\nMagazine Information:")
mag1.display_info
print(mag1.get_issue_number()+"\n")

mag2.display_info
print(mag2.get_issue_number())
