# Lecture 23: Complexity Classes Examples

## 1. Theta ($\Theta$) Notation & Complexity Classes

- **Asymptotic Complexity**: $\Theta$ notation denotes the tight bound of an algorithm's running time by looking at the dominant term as the input size grows infinitely.
- **Simplification**: Low-order terms, additive constants, and multiplicative constants are dropped to classify code into a few standard efficiency classes.

- **The Hierarchy of Complexity (From Best to Worst)**:
    - $\Theta(1)$ – **Constant** time
    - $\Theta(\log n)$ – **Logarithmic** time
    - $\Theta(n)$ – **Linear** time
    - $\Theta(n \log n)$ – **Log-linear** time
    - $\Theta(n^c)$ – **Polynomial** time (typically quadratic, $\Theta(n^2)$)
    - $\Theta(c^n)$ – **Exponential** time



---

## 2. Analysis of Complexity Classes with Code Examples

- **Constant Complexity $\Theta(1)$**
    - Completely independent of the input size.
    - Can have loops or recursive calls, but number of iterations or calls independent of size of input
    - Examples include basic arithmetic functions, fixed-range loops (e.g., `for i in range(100)`), and Python built-in operations like list indexing (`L[i]`), appending (`L.append()`), and dictionary lookups (`d[key]`).


- **Linear Complexity $\Theta(n)$**
    - Simple iterative loops that scale with the input size, or single recursive calls with constant overhead.
    - Examples include iterative or recursive factorials (`fact_iter`, `fact_recur`), summing the digits of a string, and iterative Fibonacci calculation (`fib_iter`).
    - Note that built-in Python operations like `e in L`, list slicing (`L[:mid]`), list equality checking (`L1 == L2`), and removing elements (`del(L[i])`) take linear time $\Theta(n)$.


- **Polynomial (Quadratic) Complexity $\Theta(n^2)$**
    - This commonly occurs with nested loops or nested recursive operations where each loop runs a number of times proportional to the input size.
    - Examples include checking if one list is a subset of another (`is_subset`), finding the intersection of two lists (`intersect`), and calculating the maximum distance between pairs of points (`diameter`).


- **Exponential Complexity $\Theta(c^n)$**
    - This occurs in recursive functions that generate more than one recursive call for each problem size step.
    - Examples include the naive recursive Fibonacci solution (`fib_recur`, which requires $\Theta(2^n)$ operations) and generating all power set combinations/subsets of a list (`gen_subsets`, which technically takes $\Theta(n \cdot 2^n)$ because copying/concatenating lists takes linear time).


- **Logarithmic Complexity $\Theta(\log n)$**
    - The running time grows proportionally to the logarithm of the input size, usually because the problem size is halved at every single step.
    - An interesting mathematical example is `digit_add(n)`, where looping through the digits of an integer `n` scales with its string length, which mathematically equals $\log_{10}(n)$.
    - The primary algorithmic example is **Bisection (Binary) Search**.



---

## 3. Case Study: Two Implementations of Bisection Search

The notes emphasize that different implementations of the exact same algorithm can yield different complexity classes:

1. **Implementation 1 (`bisect_search1`) $\rightarrow \Theta(n \log n)$**
    - This version slices the list recursively (`L[:half]` or `L[half:]`) to split the search space.
    - Even though it only takes $\Theta(\log n)$ recursive steps, copying the list at each level introduces a linear $\Theta(n)$ cost, degrading the total performance to $\Theta(n \log n)$.


2. **Implementation 2 (`bisect_search2`) $\rightarrow \Theta(\log n)$**
    - This optimal version utilizes a nested helper function that passes the original list alongside `low` and `high` pointer indices.
    - Because the list is never copied, each step takes constant time $\Theta(1)$, preserving the perfect $\Theta(\log n)$ logarithmic runtime.



---

## 4. Amortized Cost (Sorting vs. Searching)

- Searching an unsorted list linearly takes $\Theta(n)$.
- It **never** makes sense to sort a list just to run a single bisection search, because any valid sorting algorithm takes at least $\Theta(n)$ time just to read the elements, meaning $\text{Sort} + \Theta(\log n) > \Theta(n)$.
- However, it is highly efficient when you **sort once and search many ($K$) times**. Over a massive number of lookups, the initial sorting cost is distributed and becomes negligible, satisfying the inequality: $\text{Sort} + K \cdot \Theta(\log n) < K \cdot \Theta(n)$.

---

## 5. COMPLEXITY CLASSES SUMMARY
- Compare efficiency of algorithms
- Lower order of growth
- Using **$\Theta$ for an upper and lower("tight") bound**

- Given a function f:
    - Only look at **items in terms of the input**
    - Look at **loops**
        - Are they in terms of the input to f?
        - Are there nested loops?
    - Look at **recursive calls**
        - How deep does the function call stack go?
    - Look at **built-in functions**
        - Any of them depend on the input?