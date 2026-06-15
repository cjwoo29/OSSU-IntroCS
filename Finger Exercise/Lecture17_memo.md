# Lecture 17: Python Classes

## OBJECT
- Each is an **object**, and ever object has:
    - An internal **data representation88
    - A set of procedures for **interaction** with the object
- An object is an **instance** of a **type**
    - `1234` is an instance of an `int`
    - `"hello"` is an instance of a `str`

## OBJECT ORIENTED PROGRAMMING(OOP)
- Everything in python is an object(and has a type)
- Can **create new objecs** of some time
- Can **manipulate objects**
- Can **destroy objects**
    - Explicitly using `del` or just "forget" about them
    - python sstem will reclaim destroyed or inaccessible objects - called "garbage collection"
- Objects are **a data abstraction** that captures...
    1. An **iternal representation**
    2. An **interface** for interacting with object

## Classes vs. Instances
The lecture draws a sharp distinction between a class and an instance:

- Class (The Blueprint): Defining a class is like defining a new custom data type or a blueprint. You decide what data represents the class and what operations (methods) a user can perform.

- Instance (The Object): Creating an instance is like initializing a specific object in memory using that blueprint. For example, list is a class, while L = [1, 2] is a specific instance of that class.

- Lifecycle: Objects can be created, manipulated, and destroyed. Python automatically reclaims memory from destroyed or inaccessible objects through garbage collection.

## Creating a Custom Class: The `Coordinate` Example
```python
class Coordinate(object):
    def __init__(self, xval, yval):
        self.x = xval
        self.y = yval

    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

p1 = Coordinate(0, 0)
p2 = Coordinate(3, 4)
print(p1.distance(p2))
```

## 4. Anatomy of a Class Definition
- `__init__` Method (The Initializer): A special method used to set up data attributes when an object is first created.

- The Role of `self`: * `self` acts as a placeholder parameter within the class definition that refers to the specific instance currently being modified or accessed.

    - Without prefixing attributes with `self`. (e.g., `self.x`), variables are treated as local temporary variables rather than persistent instance variables.

- Methods (Procedural Attributes): Methods are functions defined inside a class that work specifically with instances of that class. The first argument of any method is always conventionally named `self`.

- The Dot (`.`) Operator: Used externally to access data attributes or invoke methods on an instance (e.g., `c.x` or `c.distance(origin)`). Python automatically passes the instance itself as the `self` argument when a method is called this way.

## THE POWER OF OOP
- **Bundle together objects** that share 
    - Common attributes and 
    - Procedures that operate on those attributes
- Use **abstraction** to make a distinction between how to 
implement an object vs how to use the object
- Build **layers** of object abstractions that inherit behaviors from other classes of objects
- Create our **own classes of objects** on top of Python’s 
basic classes