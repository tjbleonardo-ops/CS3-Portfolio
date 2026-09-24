# Advanced Class Relationships
## Previous Activities
[classAttrib](https://github.com/tjbleonardo-ops/CS3-Portfolio/blob/main/q1/OOPAct%20Part%20II/classAttributesMethods.md)

[classRel](https://github.com/tjbleonardo-ops/CS3-Portfolio/blob/main/q1/OOPAct%20Part%20III/classRelationships.md)
## Existing System Description:
1. The current classes that exist in the system is Subject and Task

2. The current system is somewhat flawed with the additional attribute of task_subject on class task, making it redundant and the code harder to understand.

## Inheritance Relationship
Parent: Subject

Child: Task

Explanation: The class "Task" has attributes task_name, is_completed, task_type, deadline, and task_subject, as well as methods change_completed, update_task, and __lt__. The class "Subject" contains attributes subject_name and subject_weight, as well as methods add_task, display_task, and import_task(task: Task). The child class task inherits the attributes subject_name and subject_weight from the parent class subject.

## Inheritance UML
![Inheritance](https://github.com/tjbleonardo-ops/CS3-Portfolio/blob/main/q1/images/inheritanceDiagram.png)
## Composition/Aggregation
Relationship: Aggregation

Explanation: A task can exist independently without a subject assigned to it, making it unassigned, but not necessarily non-existent.
## Advanced UML Diagram
![Advanced UML](https://github.com/tjbleonardo-ops/CS3-Portfolio/blob/main/q1/images/advancedClassDiagram.png)
## Python Implementation
[Source Code](https://github.com/tjbleonardo-ops/CS3-Portfolio/blob/main/q1/OOPAct%20Part%20IV/advancedRelationships.py)
## Test Run
![Test](https://github.com/tjbleonardo-ops/CS3-Portfolio/blob/main/q1/images/advancedTestRun.png)
## Object Diagram
![Objects](https://github.com/tjbleonardo-ops/CS3-Portfolio/blob/main/q1/images/advancedObjectDiagram.png)

## Reflection
Answers:
1. Why did you choose your inheritance relationship? Explain why your child class is a type of your
parent class.
- I chose an inheritance relationship because things like a task is-a part of a subject. The parent class subject has the attributes subject name ad subject weight, and it is easier to have the child class task to inherit the attributes to get rid of redundant code. This way, not only does using inheritance relationship through super().--init--() allow for less redundant code, but also help by allowing the class task to also add on its own attributes without affecting the main parent.
2. How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
- Inheritance reduces duplicate code by allowing the class task to inherit attributes from the parent class subject to prevent re-declaring variables. By using super().--init--(), I was able to have the attributes subject name and subject weight to be inherited by the class task, getting rid of the additional redundant attribute task subject. In addition, using the super().--init--() function helped allow the class task build off of what is already inherited data, making dynamic and easier code to debug.
3. Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship
between the two objects.
- The has-a relationship between the task and the subject is Aggregation, as a task can exist without a subject. in the code, the tasks are made through the task list array, then it is associated with a subject through methods add task and import task. This means that even if there are no subjects made through the subject list, the tasks can still exist without breaking the code, as there are no subjects to associate with.
4. What is the difference between Association from Part III and the advanced relationship you
implemented?
- The association from Part III focuses more on the interactions and association between to related or parent - child classes. On the other hand, the advanced relationship implemented in this activity focuses more on the strength of that association. In the code, the relationship between task and subject is based on Aggregation, the relationship where the contained object of an object can exist independently, and the inheritance relationship is also present through the use of super().--init--(), which was not present in Part III.
5. How does your design follow the DRY principle?
- My design follows the DRY principle, or the do-not-repeat-yourself principle by using methods like --lt-- as well as using super().--init--(). The method less than or lt is used to compare task objects to sort them without using longer sorting algorithms like bubble sort. The super().--init--() is used to inherit the attributes of the parent class subject, allowing it to use less lines of code by getting rid of duplicate string definitions.
