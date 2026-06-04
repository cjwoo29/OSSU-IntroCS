# [Lecture 6: Bisection Search](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/resources/mit6_100l_f22_lec06_pdf/)

- Suppose we know answer lies within some interval
    - Guess **midepoint** of interval
    - If not the answer, check if ** answer is greater than or less** than midpoing
    - **Change** interval
    - Repeat
- Process **cut set of things to check in half** at each stage
    - Exhaustive search reduces them from N to N-1 on each step
    - Bisection search reduces them from N to N/2
    -> Log algorithm is much **more efficient**

## SUMMARY
- For many problems, **cannot find exact answer**
- Need to seek a **"good enough" answer** using approximations (for floating point numbers)
- Bisection search work is FAST but for problems with:
    - Two **endpoints**
    - An **ordering** to the values
    - **Feedback** on guesses(too low, too high, corrrect, etc.)
- Newton-Rapshon is a smart way to find roots of a polynomial

