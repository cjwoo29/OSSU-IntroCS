# Lecture 18: Advanced Python Class Methods (Dunder Methods) & OOP Concepts

## 1. Operator Overloading via Magic Methods (Dunder Methods)

In Python, you can define or customize the behavior of built-in operators and functions for your custom classes by implementing double underscore (`__`) methods, commonly known as **Dunder methods**.

- **Documentation Reference:** [Python Data Model - Basic Customization](https://docs.python.org/3/reference/datamodel.html#basic-customization)

### Common Examples of Dunder Methods

- `__mul__(self, other)`: Implements the multiplication operator (`self * other`).
- `__str__(self)`: Defines the string representation used by `str(self)` or when calling `print(self)`.
- `__float__(self)`: Defines the behavior for converting an object to a float (`float(self)`).

### Comparison of Code Expressions (Style Guide)

While the following statements perform the exact same operation internally, there is a clear distinction in terms of readability and Pythonic style:

```python
# 1. Recommended Style (Shorthand) - The most clear, intuitive, and Pythonic way.
print(a * b)

# 2. Discouraged Style (Direct Dunder Call) - Explicitly calling a dunder method is considered bad style.
print(a.__mul__(b))

# 3. Generally Avoided Style (Explicit Class Call) - Passing 'self' manually via the class name should be avoided.
print(Fraction.__mul__(a, b))

```

## 2. The Value of OOP and Data Bundling (Encapsulation)

Bundling data (attributes) and behaviors (methods) together into a Python class provides powerful structural advantages for software development:

- **Organization & Modularity:** Keeps code highly organized and cleanly partitioned into modular, self-contained units.
- **Maintainability:** Makes code much easier to maintain, as changes inside an object rarely disrupt the rest of the program.
- **Extensibility:** Allows developers to easily build upon existing objects to construct more complex and sophisticated systems.
- **Decomposition & Abstraction at Work:**
    - **Decomposition:** Breaks complex problems down into smaller, manageable pieces (objects).
    - **Abstraction:** Hides the internal complexity of how a class works behind a consistent interface.
    - *Example:* Dunder methods are abstracted by common, everyday operations (like `*` or `+`). Behind the scenes, they are just standard methods, but they allow you to interact with diverse objects in a uniform and intuitive way.