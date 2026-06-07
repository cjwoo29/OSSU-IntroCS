# Finger Exercise Lecture 10

def all_true(n, Lf):
    """ n is an int
        Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called 
    with n as a parameter. Otherwise returns False. 
    """
    # Your code here
    for fn in Lf:
        if not fn(n):
            return False
    return True

# Examples:    
# define functions for testing
def is_even(x): return x % 2 == 0
def is_positive(x): return x > 0

# Example 1
funcs1 = [is_even, is_positive]
print(all_true(6, funcs1))   # Prints: True

# Example 2
funcs2 = [is_even, is_positive]
print(all_true(-2, funcs2))  # Prints: False