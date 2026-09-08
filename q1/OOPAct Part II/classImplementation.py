class Task:
  def __init__(self, task_name: str, task_type: str, deadline: int, is_completed: bool = False):
      self.task_name = task_name
      self.task_type = task_type
      self.__deadline = deadline
      self.__is_completed = is_completed

  def get_deadline(self):
     return self.__deadline

  def get_is_completed(self):
     return self.__is_completed

  def change_completed(self):
   while True:
      ask_completion = input("What do you want to set this task to? (Completed / Not Completed): ")
      if ask_completion == "Completed":
         self.__is_completed = True
         break
      elif ask_completion == "Not Completed":
         self.__is_completed = False
         break
      else:
         print("Try again with only [Completed] or [Not Completed]. ")      
      return self.__is_completed
  
  @classmethod
  def sort_priority(cls, task_list):
     sorted = False
     x = len(task_list)
     for i in range(x):
        for j in range(x-i-1):
           if task_list[j].get_deadline() >task_list[j+1].get_deadline():
              task_list[j], task_list[j+1] = task_list[j+1], task_list[j]
              sorted = True
        if not sorted:
           break
     
  def __str__(self):
     return f"{self.task_name}, {self.task_type}, due in {self.__deadline} day/s. {'Completed.' if self.__is_completed else 'Not Completed.'}"

  def update_task(self):
     while True:
      edit_choice = input("Do you want to edit a task? (Yes / No): ")
      if edit_choice == "Yes":
            choice = input("Which part of the task do you want to edit? (1 [Name], 2 [Type], 3 [Days Before Deadline], 4 [Cancel Editing] ): ")
            if choice == "1":
               new_task_name = input("Enter new task name: ")
               self.task_name = new_task_name
            elif choice == "2":
               new_task_type = input("Enter new task type: ")
               self.task_type = new_task_type
            elif choice == "3":
               while True:
                  new_deadline = int(input("Enter new deadline: "))
                  try:
                     if new_deadline < 0:
                        print("Deadline cannot be negative.")
                     else:
                        break
                  except ValueError:
                     print("Deadline must be a whole number.")
                  self.__deadline = new_deadline
            elif choice == "4":
               print("Task editing cancelled.")
            break
      elif edit_choice == "No":
            print("Task editing cancelled.")
            break
      else:
            print("Task editing cancelled due to invalid input. Try again.")
            

task1 = Task("ComSci OOPAct Part II", "FA", 1, False)
task2 = Task("Filipino Vlog", "AA", 18, False) 
task_list = [task1, task2]
Task.sort_priority(task_list)
for i in task_list:
   print(i)
task2.change_completed()
task1.update_task()
Task.sort_priority(task_list)
for i in task_list:
   print(i)

