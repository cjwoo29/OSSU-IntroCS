# Lecture 11 Summary: Aliasing, Cloning, and Mutability


## 1. Memory Model: Everything is an Object

In Python, every variable is a pointer (reference) to an object in memory.

* **Immutable elements** (e.g., integers, strings, tuples) cannot be modified in place.
* **Mutable elements** (e.g., lists, dictionaries) can be altered directly in memory.

## 2. Aliasing (Reference Assignment)

**Aliasing** occurs when two or more variables point to the exact same object in memory.

```python
L1 = [1, 2, 3]
L1_copy = L1  # Aliasing

```

### Key Characteristics

* No new object is allocated in memory.
* `id(L1) == id(L1_copy)` returns `True`.
* **Side Effect:** Any mutation made through `L1_copy` will instantly reflect in `L1` because they share the same house with two different names.

```python
L1_copy.append(4)
print(L1)  # Output: [1, 2, 3, 4]

```


## 3. Cloning / Shallow Copy

**Cloning (Shallow Copying)** creates a new outer list object in memory and copies the references of the elements from the original list into the new one.

```python
L1 = [1, 2, 3]
L1_copy = L1[:]  # Slicing creates a shallow copy
# Alternative: L1_copy = L1.copy() or L1_copy = list(L1)

```

### Key Characteristics

* A new outer object is created: `id(L1) == id(L1_copy)` returns `False`.
* The inner elements themselves are **aliased** (the references of the inner elements are copied).

### The Catch: Nested Mutable Objects

If the list contains only immutable elements (like numbers or strings), a shallow copy acts as a safe, independent clone. However, if the list contains **nested mutable objects** (like a list inside a list), the inner list is still aliased.

```python
# List containing a nested list
original = [100, [1, 2]]
shallow = original[:]

# 1. Mutating the outer structure (Safe)
shallow.append(200)
print(original)  # Output: [100, [1, 2]] (Unchanged)

# 2. Mutating the inner nested list (Side Effect)
shallow[1].append(3)
print(original)  # Output: [100, [1, 2, 3]] (Mutated!)

```

## 4. Deep Copy

To completely sever all ties between the original list and the copy, including all nested structures, you must perform a **Deep Copy**. This recursively copies every single object found within the structure.

```python
import copy

original = [100, [1, 2]]
deep = copy.deepcopy(original)

deep[1].append(3)
print(original)  # Output: [100, [1, 2]] (Perfectly Safe)
print(deep)      # Output: [100, [1, 2, 3]]

```

## Summary Matrix

| Operation | Syntax | Creates New Outer List? | Aliases Inner Elements? | Safe for Nested Lists? |
| --- | --- | --- | --- | --- |
| **Aliasing** | `B = A` | ❌ No | Yes | ❌ No |
| **Shallow Copy** | `B = A[:]` or `B = A.copy()` | Yes | Yes | ❌ No |
| **Deep Copy** | `B = copy.deepcopy(A)` | Yes | ❌ No | Yes |

> 💡 **Core Takeaway:** > Think of a **Shallow Copy** as allocating a new memory address (`malloc`) *only* for the outer container, while automatically aliasing all the contents inside it. When dealing with multi-dimensional data structures, always default to `copy.deepcopy()` to avoid unintended mutation bugs.