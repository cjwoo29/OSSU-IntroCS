# Lecture 12: List Comprehension, Functions as Objects, Testing, Debugging
## 1. List Comprehensions
Create a new list, by applying a function to every element of another iterable that satisfies a test
```[expression for elem in iterable if test]```

## 2. Functions Returning Functions
### Why Bother Returning Functions?
- Code can be **rewritten** without returning function objects
    ```
    def make_multiplier(n):
        def multiplier(x):
            return x * n
        return multiplier

    double = make_multiplier(2)
    triple = make_multiplier(3)
    print(double(5))  # Output: 10
    print(triple(6))  # Output: 18
    ```
- Good software design
    - Embracing ideas of **decomposition**, **abstraction**
    - Another **tool** to structure code
    ```
    # The Generator (Separates the style logic)
    def make_wrapper(symbol):
        def wrapper(text):
            print(f"{symbol} {text} {symbol}")
        return wrapper

    # Good Design: We decompose the style and abstract it into clean tools
    bracket_print = make_wrapper("[]")
    star_print    = make_wrapper("***")

    bracket_print("Hello")  # Output: [] Hello []
    star_print("Hello")     # Output: *** Hello ***
    ```
    
- Interrupting execution
    - Example of **control flow**
    - A way to achieve partial execution and use result somewhere else before finishing the full evaluation
    ```
    import time

    def setup_api_connection(api_key, server_url):
        print("[STEP 1] Validating API Key and connecting to server...")
        time.sleep(1) # Simulating heavy network connection cost
        established_session = f"Session_for_{server_url}_using_{api_key}"
        
        # Execution interrupts here. We return a function that 'holds' the session alive.
        def send_data(payload):
            print(f"[STEP 2] Sending data packet via {established_session}")
            print(f"Payload Delivered: {payload}")
            
        return send_data

    # --- At App Startup ---
    # We run Step 1, then execution is interrupted/paused.
    # The heavy connection is made once and saved into 'lazy_sender'.
    lazy_sender = setup_api_connection(api_key="SECRET_123", server_url="https://api.cs.edu")

    print("\n... hours pass, app does other things, user finally clicks upload ...\n")

    # --- Much Later in the Program ---
    # Step 2 executes instantly without rerunning the heavy Step 1 connection logic.
    user_data = {"user_id": 2026, "score": 100}
    lazy_sender(payload=user_data)
    ```

## 3. Testing and Debugging
### 3-1. Defensive Programming
Prevent bugs before they happen.
- Modularization: Breaking programs into small, isolated, and manageable functions
- Specifications(DOcstrings): Writing clear inputs, constraints, and expected outputs for every function before you write the actual code

### 3-2. Testing
Running code with specific inpouts to see if it breaks. We should input into representative categories and focus on **boundary conditions**.
- Unit Testing: Testing each function individually.
- Regression Testing: Re-running old tests after updates to ensure you didn't break existing.
- Integration Testing: Testing how all modules work together.

#### Tow Main Testing Strategies
- **Black-Box Testing**: Designed **without** looking at the code. Rely on the function's description/specifications.
- **Glass-Box Testing**: Designed **by** looking at the code. Create tests to ensure every path, loop, and if/else branch is executed at least once.

### 3-3. Debugging
Debugging is the scientific process of isolating and fixing a bug once testing proves it exists.
- The Approach: Treat it like science. Form a hypothesis, design an experiment, and change one thing at a time. Do not blindly guess.
- The Bisection Method: Place a ```print()``` statement halfway through your code.
- Common Culprits: Forgetting to handle edge cases, off-by-one errors in loops, or accidentally modifying(mutating) list passed into functions.
