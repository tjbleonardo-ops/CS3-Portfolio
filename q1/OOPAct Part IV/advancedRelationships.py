class Subject:
   def __init__(self, subject_name: str, subject_weight: int):
      self.subject_name = subject_name
      self.subject_weight = subject_weight
      self.__task_list = []
#actually adds task
   def import_task(self, task: "Task"):
      self.__task_list.append(task)
#displays subject
   def display_subject(self):
      print(f"Subject: {self.subject_name} | Weight: {self.subject_weight}")
      if not self.__task_list:
         print("There are no tasks in this subject.")
         return
      
      print("Tasks:")
      for i, task in enumerate(sorted(self.__task_list)):
         print(f" {i+1}. {task}")
      print("-------------------------------------------------------------------------")
      
#sorts task to subject
   @staticmethod
   def add_task(tasks: list, subjects: list):
      for task in tasks:
         task_added = False
         for subject in subjects:
            if task.subject_name.upper() == subject.subject_name.upper():
               subject.import_task(task)
               print("Added task to subject:", subject.subject_name)
               task_added = True
               break
         if not task_added:
            print("Task not added to any subject.")


class Task(Subject):
  def __init__(self, task_name: str, task_type: str, deadline: int, is_completed: bool = False, subject_name: str = "Other", subject_weight: int = 1):
      super().__init__(subject_name, subject_weight)

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
#replaces func "sort_priority"
  def __lt__(self, other: "Task"):
      return self.__deadline < other.__deadline

     
#individual task print    
  def __str__(self):
     return f"{self.task_name}, {self.task_type}, due in {self.__deadline} day/s. {'Completed.' if self.__is_completed else 'Not Completed'}, Subject is {self.subject_name}."

  def update_task(self):
     while True:
      edit_choice = input("Do you want to edit a task? (Yes / No): ")
      if edit_choice == "Yes":
            choice = input("Which part of the task do you want to edit? (1 [Name], 2 [Type], 3 [Days Before Deadline], 4 [Task Subject], 5 [Cancel Editing]): ")
            if choice == "1":
               new_task_name = input("Enter new task name: ")
               self.task_name = new_task_name
            elif choice == "2":
               new_task_type = input("Enter new task type: ")
               self.task_type = new_task_type
            elif choice == "3":
               while True:
                  try:
                     new_deadline = int(input("Enter new deadline: ")) #placed new deadline here because it broke too
                     if new_deadline < 0:
                        print("Deadline cannot be negative.")
                     else:
                        self.__deadline = new_deadline #i put the self deadline here because it broke because it was out of the loop
                        break
                  except ValueError:
                     print("Deadline must be a whole number.")                  
            elif choice == "4":
               new_task_subject = input("Enter new task subject: ")
               self.subject_name = new_task_subject
            elif choice == "5":
               print("Task editing cancelled.")
            else:
               print("Invalid choice. Task editing cancelled.")
            break
      elif edit_choice == "No":
            print("Task editing cancelled.")
            break
      else:
            print("Task editing cancelled due to invalid input. Try again.")

english = Subject("English",1.7)
filipino = Subject("Filipino",1)
comsci = Subject("ComSci",1)

subjects = [english, filipino, comsci]

task1 = Task("OOPAct Part III", "FA", 1, False, "ComSci")
task2 = Task("Vlog", "AA", 8, False, "Filipino") 
task3 = Task("60 Second Pitch", "AA", 3, False, "English")
task4 = Task("OOPAct Part IV", "FA", 4, True, "ComSci")


task_list = [task1, task2, task3, task4]
print("Before ---------------------------------------------------------------------\n")
for i, task in enumerate(sorted(task_list)):
   print(f" {i+1}. {task}")
print("")

print("During ---------------------------------------------------------------------\n")
Subject.add_task(task_list, subjects)
print("")

print("After ----------------------------------------------------------------------\n")

english.display_subject()
filipino.display_subject()
comsci.display_subject()




