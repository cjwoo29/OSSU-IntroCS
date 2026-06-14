# Lecture 15: Recursion
## RECURSION
- Recursion is a
    - Programmign method
    - Way to divide and conquer
- A **function calls itself**
- A problem is broken down into a **base case** and a **recursive step**

## RECURSIVE and BASE STEPS
- Recursive step
    - Decide how to reduce problem to a **simpler/smaller version** of same problem, plus simple operations.
- Base case
    - Kepp reducing problem until reach a simple case that can be **solved directly**

## WHAT IS RECURSION?
- Algorithmically: a way to design solutions to problems by **divide-and -conquer** or **decrease-and-conquer**
    - Reduce a problem to simpler versions of the same problem or to problem that can be solved directly
- Semantically: a programming technique where a **function calls itself**
    - In programming, goal is to NOT have infinite recursion
    - Must have **1 or more base cases** that are easy tosolve directly
    - Must solve the same problem on **some other input** with the goal of simplifying the larger input problem, ending at base case