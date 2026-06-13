# Lecture 14: Dictionaries

A dictionary maps each unique key to an associated value.

---

## Dictionary Operations

### Initialization

```python
grades = {'Ana':'B', 'Matt':'A', 'John':'B', 'Katy':'A'}
```

### Basic Actions

* **Add an entry:** `grades['Grace'] = 'A'`
* **Change an entry:** `grades['Grace'] = 'C'`
* **Delete an entry:** `del(grades['Ana'])`

### Key Membership Testing

>`in` operator only checks keys, not values.

```python
'John' in grades    # Returns: True
'Daniel' in grades  # Returns: False
'B' in grades       # Returns: False

```

### Accessing Keys, Values, and Items

* **Keys:** Get an iterable view of all keys

    ```python
    grades.keys()        # Returns: dict_keys(['Ana', 'Matt', 'John', 'Katy'])
    list(grades.keys())  # Returns: ['Ana', 'Matt', 'John', 'Katy']
    ```

* **Values:** Get an iterable view of all values
    ```python
    grades.values()        # Returns: dict_values(['B', 'A', 'B', 'A'])
    list(grades.values())  # Returns: ['B', 'A', 'B', 'A']
    ```

* **Items:** Get an iterable view of all `(key, value)` tuples
    ```python
    grades.items()        # Returns: dict_items([('Ana', 'B'), ...])
    list(grades.items())  # Returns: [('Ana', 'B'), ('Matt', 'A'), ('John', 'B'), ('Katy', 'A')]
    ```


### Common Iteration Pattern
```python
for k, v in grades.items():
    print(f"key {k} has value {v}")
```

---

## Dictionary Keys & Values

* Dictionaries are **mutable** objects.
* There is no guaranteed order to keys or values (Assume unordered).

### Keys

* Must be **unique**.
* Must be an **immutable** type (`int`, `float`, `string`, `tuple`, `bool`).
* Technical requirement: Needs to be a **hashable** object (all immutable types are hashable).
* ⚠️ **Be careful using `float` type as a key** (due to floating-point precision issues).

### Values

* Can be **any type** (both mutable and immutable).
* Can be lists, or even other dictionaries.
* Can be **duplicated**.

---

## Summary

* Dictionaries contain entries that **map a key to a value**.
* **Keys** must be **immutable/hashable and unique** objects.
* **Values** can be **any object**.
* Dictionaries make code highly efficient:
* Implementation-wise
* Runtime-wise ($O(1)$ average time complexity for lookups)