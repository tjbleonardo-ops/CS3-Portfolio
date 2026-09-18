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
![Class Relationship Diagram](classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?

### What multiplicity did you choose and why?
One to zero or many, since one subject can have multiple tasks.
### How did you implement the relationship in Python?
not yet
### Why did you store an object reference instead of copying its data?

### If your relationship uses many, why is a list appropriate?
Because lists store many values while acting as one variable.
