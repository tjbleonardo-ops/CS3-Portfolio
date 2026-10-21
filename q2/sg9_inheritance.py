class Publication:
  def __init__(self, title, author):
    self.__title = title
    self.__author = author
 
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
    

  def display_info(self):
    print(f"Title: {self.__title}")
    print(f"Author: {self.__author}")

class Book(Publication):
  def __init__(self, number_of_pages):
    super().__init__(title, author)
    self.__number_of_pages = number_of_pages

  def get_number_of_pages(self):
    return self.__number_of_pages

  def set_number_of_pages(self, number_of_pages):
    if number_of_pages < 0:
      print("Number of pages must be positive.")
    else:
      self.__number_of_pages = number_of_pages
      
class Magazine(Publication):
  def __init__(self, issue_number):
    super().__init__(title, author)
    self.__issue_number = issue_number

  def get_issue_number(self):
    return self.__issue_number

  def set_issue_number(self, issue_number):
    if issue_number < 0:
      print("Issue number must be positive.")
    else:
      self.__issue_number = issue_number

pub1 = Publication("hi","test")
pub1.display_info

pub2 = Publication("hie","teste")
pub2.display_info
#Add data validation to number_of_pages and issue_number. Display a message such as “The number of pages must be positive” if the value is zero or negative.



