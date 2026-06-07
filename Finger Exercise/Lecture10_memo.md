# Lecture 10: Lists, Mutability

## STRINGS to LISTS
- Convert **string to list** with ```list(s)```
- Use ```s.split()```, to **split a string on a character** parameter, splits on spaces if called without a parameter
```
s = "I<3 cs &u"
L = list(s) # L is ['I', '<', '3', ' ', 'c', ...]

L1 = s.split(' ') # L1 is ['I<3', 'cs', '&u?']
L2 = s.split('<') # L2 is ['I', '3 cs &u?']
```

## LISTS to STRINGS
- Use ```''.join(L)``` to turn a **list of strings into a bigger string**
- Can give a character in quotes to add char between every element
```
L = ['a', 'b', 'c'] # L is a list
A = ''.join(L) # A is "abc"
B = '_'.join(L) # B is "a_b_c"
C = ''.join([1,2,3]) # an error
C = ''.join(['1', '2', '3',]) # C is "123"
```
## SUMMARY
- Lists and tuples provide a way to organize data that naturally
supports iterative functions
- Tuples are **immutable** (like strings)
    - Tuples are useful when you have **data that doesn’t need to change**. e.g. (latitude, longitude) or (page #, line #)
- Lists are **mutable**
    - You can modify the object by **changing an element** at an index
    - You can modify the object by **adding elements** to the end
    - Will see many more operations on lists next time
    - Lists are useful in **dynamic situations**. e.g. a list of daily top 40 songs or a list of recently watched movies