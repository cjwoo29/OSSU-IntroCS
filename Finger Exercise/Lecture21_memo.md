# Lecture 21: Timing Programs, Counting Operations


## EFFICIENCY IS IMPORTANT
- Separate **time and space efficiency** of a program
- Tradeoff between them: can use up a bit more memory to stroe values for quicker lookup later

### EVALUATING PROGRAMS
- Measeure with a **timer**
- **Count** the operations
- Abstract notion of **order of growth**

## TIMING 
Use time module
```python
import time
def c_to_f(c):
    return c*9.0/5 +32

tstart = time.time() # Start clock
c_to_f(37) # Call function(Operate Program)
dt = time.time() -tstart # Stop clock
print(dt, "s, ")
```
But TIMING PROGRAMS IS INCONSISTENT
- Goal: to evaluate differnet algorithms
- ✔️ Running time should vary between algorithms
- ❌ Running time should not vary between implementations
- ❌ Running time should not vary between computers
- ❌ Running time should not vary between languages
- ❌ Running time is should be predictable for small inputs

## COUNTING OPERATIONS
- Assume these steps take **constant time**:
    - Mathematical operations, Comparisons, Assignments, Accessing objects in memory
- Count number of operations executed as function of size of input

However

- No matter what the input is, the number of **operations is the same**
- As the input increases **by 10**, the number if operations ran is approx. **10 times more**

COUNTING OPERATIONS IS INDEPENDENT OF COMPUTER VARIATIONS, BUT ...
- Goal: to evaluate different algorithms
- ✔️ Running “time” should vary between algorithms
- ❌ Running “time” should not vary between implementations
- ✔️ Running “time” should not vary between computers
- ✔️ Running “time” should not vary between languages
- ✔️ Running “time” is should be predictable for small inputs
- ❌ No real definition of which operations to count

## STILL NEED A BETTER WAYH
_ Timing and counting **evaluate implementations** and **machines**
- Want to **evaluate algorithm**
- Want to **evaluate scalability**
- Want to **evaluate in terms of input size**