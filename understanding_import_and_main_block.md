# 📚 Python: import vs from ... import, and **name** == "**main**" Explained

This documentation summarizes the key concepts you have learned about Python modules, imports, and the special `__name__ == "__main__"` behavior. Real-life examples are included to reinforce understanding.

---

## ✅ 1. What is `import` in Python?

The `import` keyword allows you to load a module (Python file) and access its functions, variables, and classes.

### Syntax:

```python
import module_name
```

### Example:

```python
import math
print(math.sqrt(16))  # Output: 4.0
```

---

## ✅ 2. What is `from ... import` in Python?

This syntax allows you to import specific items (function, class, variable) from a module directly.

### Syntax:

```python
from module_name import item_name
```

### Example:

```python
from math import sqrt
print(sqrt(25))  # Output: 5.0
```

---

## 🤔 Difference Between `import` vs `from ... import`

| Feature                   | `import module` | `from module import item`      |
| ------------------------- | --------------- | ------------------------------ |
| Imports                   | Entire module   | Specific part (function/class) |
| Usage                     | `module.item()` | `item()` directly              |
| Namespace collision risk  | Low             | Higher if same name exists     |
| Best for large module use | Yes             | No                             |
| More concise              | No              | Yes                            |

---

## 🤓 Special Variable: `__name__`

In every Python file, there's a built-in variable called `__name__`.

### Behavior:

| How the file is used          | Value of `__name__`            |
| ----------------------------- | ------------------------------ |
| Run directly (python file.py) | `"__main__"`                   |
| Imported from another module  | module name (e.g., `mymodule`) |

---

## ✨ What is `if __name__ == "__main__":`?

This line checks whether the script is being run **directly**. If true, it runs a specific block of code (like `main()`).

### Syntax:

```python
def main():
    print("Running main function")

if __name__ == "__main__":
    main()
```

### Why use this?

* Prevents code from running during import
* Makes your code reusable as a module
* Keeps script behavior and module behavior separate

---

## 🏠 Example with Multiple Functions

### File: `mymodule.py`

```python
def greet():
    print("Hello from greet!")

def add(a, b):
    return a + b

if __name__ == "__main__":
    greet()
    print(add(2, 3))
```

### File: `main.py`

```python
from mymodule import greet, add

greet()            # Works fine
print(add(5, 6))    # Output: 11
```

> Note: greet() inside `mymodule.py` will **not** auto-run during import because it is inside `__main__` block.

---

## 🚀 Bonus: Using `as` for Aliases

```python
import numpy as np
from math import sqrt as s

print(np.array([1, 2, 3]))
print(s(49))  # Output: 7.0
```

---

## 🔧 When to Use What?

| Goal                                 | Use This                  |
| ------------------------------------ | ------------------------- |
| Use full module with less collision  | `import module`           |
| Use only 1-2 functions from a module | `from module import item` |
| Rename for short use or conflict     | `import module as alias`  |

---

## ✅ Summary:

* `import` loads the full module
* `from ... import` gets specific items
* `__name__ == "__main__"` ensures your code only runs when script is executed directly
* Helps you separate script logic and module logic

---
