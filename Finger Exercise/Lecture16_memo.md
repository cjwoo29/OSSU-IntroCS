# Lecture 16: Recursion on Non-Numerics
Each case(base cases, recursive step) must return the same type of object.
## PROBLEMS that are NATURALLY RECURSIVE
- A file system
- Order of operations in a calculator
- Scooby Doo gang searching a haunted castle
- Bureaucracy

## MAJOR RECURSION TAKEAWAYS
- Most problems are solved more **intuitively with iteration**
    - We show recursion on these to:
        - Show you a **different way of thinking** about the same problem (algorithm)
        - Show you **how to write a recursive function** (programming)
- Some problems have **nicer solutions with recursion**
    - If you recognize solving the same problem repeatedly, use recursion
- Tips
    - Every case in your recursive function **must return the same type of thing**
    - Your function **doesn't have to be efficient on the firt pass**
        - It's ok to have more than 1 base case
        - It's **ok to break down the problem** into many if/elifs
        - As long as you are **making progress** toward a base case recursively
