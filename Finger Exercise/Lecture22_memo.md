# Lecture 22: Big Oh and Theta

## PROBLEMS WITH TIMING AND COUNTING
- Timing the exact running time of the program
    - Depends on machine
    - Depends on implementation
    - Small inputs don’t show growth
- Counting the exact number of steps
    - Gets us a formula!
    - Machine independent, which is good
    - Depends on implementation
    - Multiplicative/additive constants are irrelevant for large inputs
- Want to:
    - evaluate **algorithm**
    - evaluate **scalability**
    - evaluate **in terms of input size**

---

## ORDER of GROWTH
- It's a notation
- Evaluates programs when **input is very big**
- Expresses the **growth of program's run time**
- Puts an **upper bound** on growth
- Do not need to be precise: **"order of" not "exact"** growth
- Focus on the **largest factors** in run time (which section of the program will take the longest to run?)

### A BETTER WAY A GENERALIZED WAY WITH APPROXIMATIONS
- Use the idea of counting operations in an algorithm, but **not worry about small variations in implementation**
    - When x is big, 3x+4 and 3x and x are pretty much the same!
    - Don’t care about exact value: ops = 1+x(2+1)
    - Express it in an “order of” way vs. the input: ops = Order of x
- Focus on how algorithm performs when **size of problem gets arbitrarily large**
- **Relate time** needed to complete a computation **against the size of the input** to the problem
- Need to decide what to measure. What is the input?

### WHICH INPUT TO USE TO MEASURE EFFICIENCY
- Want to express **efficiency in terms of input**, so need to **decide what is your input**
- Colud be an interger or length of list etc.
- **You decide** when multiple parameters to a function

### ASYMPTOTIC GROWTH
- Goal: describe how time grows as size of input grows
    - Formula relating input to number of operations
- Given an expression for the number of operations needed to compute an algorithm, want to know asymptotic behavior as size of problem gets large
    - Want to put a bound on growth
    - Do not need to be precise: “order of” not “exact” growth
- Will focus on term that grows most rapidly
    - Ignore additive and multiplicative constants, since want to know how rapidly time required increases as we increase size of input
- This is called **order of growth**
    - Use mathematical notions of "big O" and "big Θ"
Big Oh and Big Theta

Here is the ultra-short version:


### Big O vs. Big Theta

- **Big O ($O$) = Upper Bound (Ceiling)**
    - $$\exists c > 0, n_0 > 0 \quad \text{such that} \quad 0 \le f(n) \le c \cdot g(n) \quad \forall n \ge n_0$$
    - "My code will **never run worse** than this."


- **Big $\Theta$ ($\Theta$) = Tight Bound (Exact Match)**
    - $$\exists c_1 > 0, c_2 > 0, n_0 > 0 \quad \text{such that} \quad 0 \le c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n) \quad \forall n \ge n_0$$
    - "My code runs at **this exact rate**."

### Key Difference

- If $f(n) = 2n + 5$:
    - It is **O(n), O($n^2$), and O($n^3$)** (all are valid ceilings).
    - It is **only $\Theta$(n)** (exact match).


- **$\Theta$ is a subset of O.** $\Theta$ is always more precise and informative than O.