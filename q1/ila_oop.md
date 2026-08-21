# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulating variables like product name, price, quantity in a single "Product" class would make it so that external code would not be able to directly modify quantity variables to prevent errors or possible data corruption. This makes it more viable than using separated variables, as with separated variables, code does not need to be too redundant as well.

### 2. Abstraction
Abstraction is the process of hiding specific actions and displaying a clean, wrapped up version of the code. We can apply abstraction in this problem by having the user or sari - sari owner only interact with actions without needing to know how arithmetic or internal assignments are executed, simplifying the design by separating the usage of an object from its implementation details.

### 3. Inheritance
Inheritance is the ability specified product categories to inherit the foundational attributes of the main Product class while also customizing how those attributes are handled. A DiscountProduct class can inherit the three main attributes of the main Product class, and then use those attributes without disrupting the main Product class.

### 4. Polymorphism
Polymorphism is defined as “the condition of occurring in several different forms”. It means that we can call the same method on different objects. We can use this by creating a function like total_value() and assigning it to things like 25% discounts, and having the main total value calculation be integrated into that discount, getting rid of redundant code.

## Reflection
Encapsulation is by far the most useful for improving the sari - sari store inventory calculation. Encapsulation helps by grouping the three variables in a single class, and then implementing validation whenever the price or quantity are modified. In a system where these variables are separated, it can be easy to accidentally enter a different value for a different variable and cause errors. 
