# Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md)

[classRel](classRelationships.md)
## Existing System Description:

## Inheritance Relationship
Parent: Subject

Child: Task

Explanation: The class "Task" has attributes task_name, is_completed, task_type, deadline, and task_subject, as well as methods change_completed, update_task, and __lt__. The class "Subject" contains attributes subject_name and subject_weight, as well as methods add_task, display_task, and import_task(task: Task). The child class task inherits the attributes subject_name and subject_weight from the parent class subject.

## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)
## Composition/Aggregation
Relationship: Aggregation

Explanation: A task can exist independently without a subject assigned to it, making it unassigned, but not necessarily non-existent.
## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
![Test](images/advancedTestRun.png)
## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
Answers:
1. Why did you choose your inheritance relationship? Explain why your child class is a type of your
parent class.
-
2. How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
-
3. Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship
between the two objects.
-
4. What is the difference between Association from Part III and the advanced relationship you
implemented?
-
5. How does your design follow the DRY principle?
-
