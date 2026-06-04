# [Lecture 8: Functions as Objects](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/resources/mit6_100l_f22_lec08_pdf/)
Everything in Python is an object. Functions are also an **first class object**. Therefore the function can play a role as a parameter.


```
def calc(op, x, y):
    return op(x, y)

def add(a, b):
    return a + b

print(calc(add, 2, 3))
```

## SUMMARY
- Functions are first class objects
    - They have a **type**
    - They can be **assigned as a value** bound to a name
    - They can be used as an **argument** to another procedure
    - They can be **returned** as a value from another procedure
- Have to be careful about environments
    - Main program runs in the global environment
    - Function calls each get a new temporary environment
- This enables the creation of concise, easily read code

