# SG4 - Understanding Classes and Objects
## Class Name
Task
## Class Description
This class is used in the context of an online task / homework manager. This class contains data fields such as the name of a task, it's deadline, whether or not the task has been completed, and also what the type of task it is.
## Properties
| Property | Data Type | Description |
|---|---|---|
| Task Name | String | This property of the object is the name of the task set by the user.|
| Deadline | Integer | This integer property of the object is the deadline of that specific task. |
| Completed | Boolean | This property tells whether or not the task is done or not. This property is set to false automatically. |
| Type of Task | String | This property is set by the user and tells the type of task it is (AA, FA, Group Project, etc.) |
## Methods
| Method | Description |
|---|---|
| sortpriority() | Makes all tasks return a value of Deadline - datetoday, and outputs all tasks in order of what task's deadline is closest to today's date.|
| changeCompleted(complete : boolean) | Allows the user to change the "Completed" property of the task. |
| updateTask() | Allows the user to update the task's name, deadline, or type of task.|
## Class Diagram
![Class Diagram]()
## Design Explanation
### Why did you choose this class?
Because it is especially important in times like compliance period or when trying to organize what I'm trying to do. 
### Which property is the most important? Why?
The task name, since it allows the specific child tasks to be identified quickly and to reduce confusion on which task is which.
### Which method is the most useful? Why?
sortpriority(), since it allows the user to automatically sort all tasks by due date and reorganize their thoughts.
