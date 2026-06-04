# [Lecture 7: Decomposition, Abstraction, Functions](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/resources/mit6_100l_f22_lec07_pdf/)
## AN EXAMPLE: the smartphone abstraction
- Abstraction
    - User **doesn't know the details** of how it works
    - User **does know the interface**
    - Know **relationship** between input and output
- Decomposition
    - Designed and made by different companies.
    - Each component maker has to know **how its componenet interfaces** to other components
    - Each component maker can **solve subproblems independent of other parts**, so long as they provide specified inputs
    - True for hardward and for software

-> Apply abstarction and decomposition to programming

## Supress Details with ABSTRACTION
- In programming, want to think of piece of code as **black box**
    - Hide tedious coding details from the user
    - Reuse black box at different parts in the code
- Coder creates details, but **user doesn't need or want** to see details
- Coder achieves abstraction with a **function (or procedure)** which lets us captur code within a black box.

## Create Structure with DECOMPOSITION
- Given the idea of black box abstraction, use it to divide code into modules that are:
    - **Self-contained**
    - Intended to be **reusable**
- Modules are used to:
    - **Break up** code into logical pieces
    - Keep code **organized**
    - Keep code **coherent** (readable and understandable)
- We can achieve decomposition with functions and classes

## FUNCTIONS
- Has a name
- Has (formal) parameters (0 or more)
- Has a docstring (optional but recommended)
    - A comment delineated by """ that provides a **specification** for the function - contract relating output and input
    - It can be called by ```my_func.__doc__```
- Has a body
- Reutrns something

## SUMMARY
- Functions allow us to **suppress detail** from a user
- Functions **capture computation** within a black box
- A programmer writes functions with
    - 0 or more **inputs**
    - Something to **return**
- A function only **runs when it is called**
- The entire function call is **replaced with the return value**