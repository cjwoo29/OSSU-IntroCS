# Lecture 13: Exceptions, Assertions

## 1. EXCEPTIONS
Python code can provide **handlers** for exceptions
```
try:
    # do some potentially problematic code
except:
    # do someting to handle the problem
```
### Extended Exception Structures
- The ```else``` Block: Code inside this block runs only if the ```try``` block complete successfully without any exceptions.
- The ```finally``` Block: Code inside this block **always runs**, no matter what.

## 2. ASSERTIONS
Assertions are structured checkpoints designed to verify that the core assumptions underlying a computation are exactly as expected.
```
assert <condition>, "Optional error message if False"
```
