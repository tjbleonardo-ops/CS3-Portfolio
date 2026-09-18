# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](https://github.com/tjbleonardo-ops/CS3-Portfolio/blob/main/q1/classObjectUML.md)

[Part II - Class Attributes and Methods](https://github.com/tjbleonardo-ops/CS3-Portfolio/blob/main/q1/OOPAct%20Part%20II/classAttributesMethods.md)
## Existing Class
Class: Task

Description: The blueprint of task objects. Has attributes such as task_name, is_completed, task_type, deadline.

## New Related Class
Class: Subject

Description: Stores and sorts task objects into the subject objects based on the task object's assigned subject.

## Association
Relationship: Subject contains a Task

Explanation: The subject contains zero or many tasks that are from that subject, and stores their data while also having a function that summarizes the list of tasks in each subject.

## Multiplicity
Multiplicity: Subject 1 ------- 0..* Tasks

Explanation: Tasks are organized by their subject class, where the subject class also stores multiple tasks that belong to it.

## UML Class Relationship Diagram
[Class Relationship Diagram](https://github.com/tjbleonardo-ops/CS3-Portfolio/blob/main/q1/images/objectRelationshipDiagram.png)
## Python Implementation
[View Python Source](https://github.com/tjbleonardo-ops/CS3-Portfolio/blob/main/q1/OOPAct%20Part%20III/classRelationships.py)
## Test Run
[Relationship Test Run](https://github.com/tjbleonardo-ops/CS3-Portfolio/blob/main/q1/images/relationshipTestRun.png)
## Object Relationship Diagram
[Object Relationship Diagram](https://github.com/tjbleonardo-ops/CS3-Portfolio/blob/main/q1/images/classRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
The association between the two classes is a container relationship where Subject has a or many tasks. In the program, the Subject holds zero or many tasks, and each task has an attribute task_subject, which allows it to be automatically sorted into its designated subject. This association allows subject objects to display the tasks stored in them and sort them by due date, without disrupting the original task attributes.

### What multiplicity did you choose and why?
One to zero or many. I chose this multiplicity since a single real life subject can have multiple tasks or none at all, and if I had made my code assigned for a one to one or many, then there would always have to be one task in the subject even if there are no tasks given by the teacher. Overall, the zero to many multiplicity makes arranging and storing tasks easier, while also not worrying what will happen if there are no tasks in a subject.

### How did you implement the relationship in Python?
I implemented the relationship by first initializing an extra attribute to the already existing task class, called task_subject. After that, the related class Subject was made with attributes subject_name and subject_weight, as well as three methods such as import_task, display_task, and add_task. The add_task checks every task object's task_subject attribute to see if it matches with the subject's subject_name, and if it did, it added it to the self.__task_list, which stores the task objects assigned to that subject.

### Why did you store an object reference instead of copying its data?
Storing an object reference helps make the displayed data of the subject update automatically if the data of a task in that subject is changed. If the data was copied, then updated, the task would not update on the subject display. Storing the object references makes it so that the output is more consistent and less prone to errors.

### If your relationship uses many, why is a list appropriate?
Because lists store many values while acting as one variable. Lists can be easily sorted with the sorted() function and make the sort by deadline feature possible, and easier to code or debug. Lists are also dynamic when it comes to adding and removing items, and work well with storing multiple values, which is why a list is appropriate for a one to many relationship.

## Changes:
-Replaced sort_priority with lt function
-Added task_subject to task attributes
