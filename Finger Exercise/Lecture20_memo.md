# Lecture 20: Fitness Tracker Object-Oriented Programming Example

## WHY INFORMATION HIDING?

- **Keep the interface simple:** Maintain the class interface as minimal and clean as possible.
- **Use getters & setters instead of direct attributes:** - e.g., Use the `get_calories()` method rather than accessing the `calories` attribute directly.
    - This prevents bugs when the internal implementation changes.


- **Scalability matters:** While direct access may seem inconsequential in small programs, complex interfaces significantly increase the potential for bugs in large-scale applications.
- **API Commitment:** If you are writing a class for others to use, you are committing to maintaining and supporting its interface.

## WHY USE INHERITANCE?

- **Improve clarity:** - Commonalities are explicitly defined in the parent class.
    - Differences and unique behaviors are explicitly defined in the subclass.


- **Code reuse:** Avoid duplication by inheriting existing functionality.
- **Enhance modularity:** Subclasses can be seamlessly passed to any method or function that expects the parent class (Polymorphism).

## OVERRIDING & METHOD RESOLUTION

- **Method Overriding:** A subclass defines a method with the exact same name as a method in its superclass to provide specific behavior.
- **Method Lookup Order (Control Flow):** - When a method is called on an instance, Python first looks for it within the **current class definition**.
- If not found, it searches **up the class hierarchy**.
- It executes the first matching method found during this upward search.



## OBJECT-ORIENTED DESIGN: MORE ART THAN SCIENCE

- OOP is a powerful paradigm for **modularizing** code and binding state (data) and behavior (functions) together.

**However, keep in mind:**

- **Avoid over-engineering:** New OOP programmers often build overly elaborate and complex class hierarchies, which is rarely a good idea.
- **Focus on the user:** Always consider the developers who will use your code—*will your decomposition and structure make sense to them?*
- **Implicit complexity:** Because the invoked method is determined implicitly by the class hierarchy, tracking and reasoning about the control flow can sometimes be difficult.
- **Develop your own taste:** The internet is full of conflicting opinions on OOP and "good software design." Ultimately, you must develop your own intuition and design principles through hands-on experience.