# Lecture 9: Lambda Functions, Tuples, and Lists

## ANONYMOUS FUNCTIONS(lambda function)
Can use an **anonymous** procedure by using *lambda*

```
lambda x: x%2 == 0
```

Function call with an anonymous function as parameter:

```
def do_twice(n, fn):
    return fn(fn(n))
print(do_twice(3, lambda x: x**2))
```
*lambda* functions is **one-time use**.

## TUPLES
- **Indexable ordered sequence** of objects
- Cannot change element values, **immutable**
- Used to **return more than one value** from a function
    ```
    def quotient_and_remainder(x,y):
        q = x // y
        r = x % y
        return (q, r)
    
    (quot, rem) = quotient_and_remainder(5, 2)
    ```

### VARIABLE NUMBER of ARGUMENTS
```
def mean(*args):
    tot = 0
    for a in args: 
        tot += a
    return tot / len(args)

mean(1, 2, 3, 4, 5, 6)
```

*args means packing all incoming arguments into a single tuple, regardless of how many there are.

## LIST
- **Indexable ordered sequence** of objects
- **Mutable**, this means you can change values of specific elements of list

## SUMMARY
- Lambda functions are useful when you need a simple function
once, and whose body can be written in one line
- Tuples are indexable sequences of objects
    - Can’t change its elements, for ex. can’t add more objects to a tuple
    - Syntax is to use ()
- Lists are indexable sequences of objects
    - Can change its elements. Will see this next time!
    - Syntax is to use []
- Lists and tuples are very similar to strings in terms of
    - Indexing,
    - Slicing,
    - Looping over elements