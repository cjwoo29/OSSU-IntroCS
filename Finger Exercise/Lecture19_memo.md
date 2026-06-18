# Lecture 19: Inheritance

## 1. Getter and Setter Methods

It is highly recommended to use **Getter** and **Setter** methods to access and modify data attributes from outside a class, rather than interacting with the attributes directly.

### Example of Data Encapsulation

```python
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)
    def get_age(self):      # Getter: Safely retrieves the attribute value
        return self.age
    def set_age(self, newage): # Setter: Safely updates the attribute value
        self.age = newage

```

* **The Reason:** The author of the class definition might **change the internal variable names** of the data attributes at any time.
* **The Risk:** If your external code accesses data attributes directly (e.g., `instance.age`) and the underlying class definition changes, your code will break and throw errors.

## 2. Hierarchies and Inheritance

Inheritance allows us to create structured relationships between classes, enabling a new class to adopt and extend the functionality of an existing one.

* **Parent class (Superclass)**
* **Child class (Subclass)**
* **Inherits** all data and behaviors from the parent class.
* **Adds** more information (attributes).
* **Adds** more behavior (methods).
* **Overrides** existing parent behaviors to change how they work.


## 3. Implementing Subclasses and Method Resolution

### Basic Inheritance & Overriding (`Cat` Class)

```python
class Cat(Animal):
    def speak(self): # Adds a completely new behavior
        print("meow")
    def __str__(self): # Overrides the parent's __str__ method
        return "cat:" + str(self.name) + ":" + str(self.age)

```

* Even though `__init__` is not explicitly defined in the `Cat` class, it automatically utilizes the inherited `Animal` version.
* **Method Lookup Mechanism:** When a method is called on an object, Python looks for that method name in the **current class definition** first. If it is not found, Python searches **up the hierarchy** and executes the first matching method it encounters.

### Calling the Parent Constructor (`Person` Class)

```python
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age) # Explicitly calls the parent constructor
        self.set_name(name)         # Adds a new data attribute via a method
        self.friends = []
    def get_friends(self):
        return self.friends.copy() # Returns a copy to protect the original list
    def speak(self):
        print("hello")
    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.age)

```

* In the subclass `__init__`, you can invoke `Animal.__init__(self, age)` to run the initialization lines of code defined inside the parent class.

> **💡 Key Takeaway:** A subclass can **use** a parent's attributes, **override** a parent's attributes, or **define completely new** attributes.

## 4. Class Variables

```python
class Rabbit(Animal):
    # Class variable: Shared across all instances of this class
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.p1 = parent1
        self.p2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1 # Increments the shared class variable

```

* **Class Variables (`tag`):** Unlike instance variables, class variables are **shared across every instance** of that class.
* If one instance or the class itself alters this variable, the change is instantly reflected across all other instances.

## 5. The Ultimate Value of Object-Oriented Programming (OOP)

* **Custom Collections of Data:** Allows you to design specialized data types tailored to your specific problem.
* **Information Organization:** Keeps complex data highly structured, intuitive, and clean.
* **Division of Work:** Facilitates collaborative development by isolating system components into self-contained objects.
* **Consistent Access:** Enables users to interact with data in a predictable, uniform manner.
* **Layers of Complexity:** Helps build sophisticated software architectures via class hierarchies, where child classes cleanly inherit and scale up parent data and methods.
* **Decomposition and Abstraction:** Much like functions, classes serve as a foundational mechanism for breaking down massive problems (Decomposition) and hiding low-level implementation details (Abstraction) in modern programming.