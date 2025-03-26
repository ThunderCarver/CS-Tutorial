# [Python's Instance, Class, and Static Methods demystified](https://realpython.com/instance-class-and-static-methods-demystified/?utm_source=notification_summary&utm_medium=email&utm_campaign=2025-03-18)

- [Compare Instance Methods, Class Methods, and Static Methods](#compare-instance-methods-class-methods-and-static-methods)
- [Gain Insight Through an Abstract Example](#gain-insight-through-an-abstract-example)
- [Apply your Knowledge With a Practical Example](#apply-your-knowledge-with-a-practical-example)
  - [When to use Instance Methods](#when-to-use-instance-methods)
  - [When to use Class Methods](#when-to-use-class-methods)
  - [When to use Static Methods](#when-to-use-static-methods)
- [Conclusion](#conclusion)

Instance, class, and static methods each serve a distinct role in Python, and knowing when to use one over another is key to writing clean, maintainable code. Instance methods operate on individual objects using self, while class methods use cls to access class-level data. Static methods, on the other hand, provide organizational structure without relying on class or instance state.

When you understand the differences between these three method types, you’ll be in a better spot to know when to write an instance method, class method, or a static method. Ultimately, this’ll help you design better maintainable object-oriented Python code.

**By the end of this tutorial, you’ll understand that:**

- [ ] **Instance methods** access the state of a **specific object** through the self parameter. You create **class methods** with the **@classmethod** decorator and use them for operations that involve **class-level data**.
- [ ] You use **static methods** for **utility functionality** that doesn’t need class or instance data, and you create them with the **@staticmethod** decorator.
- [ ] Using class methods and static methods in your classes can **improve class design** and **code maintainability**.

If you develop an intuitive understanding for their differences, you’ll be able to write object-oriented Python code that communicates its intent more clearly and is easier to maintain in the long run.

## Compare Instance Methods, Class Methods, and Static Methods

If you’re here for a quick reminder of how the three method types differ from one another, then consider the following overview that compares them:

| Method Type | Description | Usage |
|-------------|-------------|-------|
| Instance Methods | Operate on specific object instances | `self` parameter |
| Class Methods | Operate on class-level data | `cls` parameter |
| Static Methods | Utility functions, no dependencies on class or instance | No parameters |

- **Instance methods** use a `self` parameter pointing to an instance of the class. They can access and modify **instance state** through `self` and **class state** through `self.__class__`. These are the most common methods in Python classes.

- **Class methods** use a `cls` parameter pointing to the class itself. They can modify **class-level state** through `cls`, but they can’t modify individual instance state.

- **Static methods** don’t have access to cls or self. They behave like plain functions except that they’re included in a class body.

Here are the most important aspects of the three different types of methods in Python classes summed up in a table:

| Type | Decorator | Parameter | Instance Access | Class Access | Use Case |
|------|-----------|-----------|-----------------|--------------|----------|
| Instance | None needed | self | ✅ | ✅ | Operations on individual instances. |
| Class | @classmethod | cls | ❌ | ✅ | Factory methods, alternative constructors, or any method that deals with class-level data. |
| Static | @staticmethod | No self or cls | ❌ | ❌ | Utility methods that don’t need instance or class data. |


Next, the differences between instance, class, and static methods in a somewhat abstract code example will be explored.

## Gain Insight Through an Abstract Example

a small Python file called demo.py with a bare-bones Python class that contains stripped-down examples of all three method types:

```python
class DemoClass:
    def instance_method(self):
        return 'Instance method called', self

    @classmethod
    def class_method(cls):
        return ("class method called", cls)

    @staticmethod
    def static_method()
        return ("static method called",)  
```

Inside demo.py, you create DemoClass—a descriptively named custom class with the sole purpose of demoing the differences between instance methods, class methods, and static methods.

```python
from demo import DemoClass
>>> obj = DemoClass()

>>> obj.instance_method()
('instance method called', <demo.DemoClass object at 0x100a30d70>)

>>> obj.class_method()
('class method called', <class 'demo.DemoClass'>)

>>> obj.static_method()
('static method called',)
```

When you call the instance method, Python replaces the self argument with the instance object, `obj`.

Like the second example shown in above snippet. The `class_method` can be accessed by instance as well. Instance methods can also access the class itself through the `self.__class__` attribute. This makes instance methods powerful in terms of access restrictions. They can modify state on the object instance and on the class itself.

You get your information message as output but no additional objects. This confirms that static methods can neither access the object instance state nor the class state. They work like regular functions but belong to the namespace of the class. They also belong to the namespace of each instance.

> Were you surprised that you can successfully call .static_method() directly on the instance object? Behind the scenes, Python enforces access restrictions by not passing in self or cls when you call a static method using the dot notation.

Now, let's take another example to see how the three methods work if without an instance of the class.
```python
from demo import DemoClass

>>> DemoClass.static_method()
('static method called',)

>>> DemoClass.class_method()
('class method called', <class 'demo.DemoClass'>)

>>> DemoClass.instance_method()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: instance_method() missing 1 required positional argument: 'self'
```

You’re able to call .class_method() and .static_method() just fine, but attempting to call .instance_method() fails with a TypeError.

Now that you’ve worked through this bare-bones example and have a better understanding of how the different method types work, you’re ready to look at a more realistic example of when to use each of the three method types.

## Apply your Knowledge With a Practical Example

The basic example from the previous section shows the distinction between instance methods, class methods, and static methods. However, it’s quite abstract and doesn’t give you a good idea of why and when you might want to use one method type over another. To connect what you learned with the real world, you’ll now explore this topic with a more realistic example.

```python
class Pizza:
    def __init__(self, toppings):
        self.toppings = list(toppings)

    def __repr__(self):
        return f"Pizza({self.toppings})"
```

### When to use Instance Methods

```python
class Pizza:
    # ...

    def add_topping(self, topping):
        self.toppings.append(topping)

    def remove_topping(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)
```

With this edit to pizza.py, you add two new instance methods that can change the state of a Pizza instance—allowing you to add and remove toppings to satisfy your customers’ every taste bud. You can now call these instance methods:

```python
>>> from pizza import Pizza
>>> a_pizza = Pizza(["cheese", "tomatoes"])
>>> a_pizza
Pizza(['cheese', 'tomatoes'])

>>> a_pizza.add_topping("garlic")
>>> a_pizza
Pizza(['cheese', 'tomatoes', 'garlic'])

>>> a_pizza.remove_topping("cheese")
>>> a_pizza
Pizza(['tomatoes', 'garlic'])
```

So, when should you use instance methods? **In short, you should use instance methods when you need to access and edit the data that an instance of your class holds**.

### When to use Class Methods

You use a class method when you need to *access or modify class-level data, such as class attributes*. Another common use case for @classmethod is to create factory methods that return class instances with specific configurations.

The Italians figured out their pizza taxonomy centuries ago, so each delicious type of pizza has its own name. It’s a good idea to take advantage of that rich pizza history and give the users of your Pizza class a better interface for creating the types of pizza they crave. A nice, clean way to do that is by using class methods as factory methods for the different kinds of pizza you can create:

```python
class Pizza:
    # ...

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomatoes"])

    @classmethod
    def prosciutto(cls):
        return cls(["mozzarella", "tomatoes", "ham"])
```

Note how the `.margherita()` and `.prosciutto()` factory methods use the `cls` argument instead of calling the `Pizza` constructor directly.

You can use the factory methods to create new Pizza objects that are configured the way you want them. They all use the same `.__init__()` constructor internally and simply provide a shortcut for remembering the various toppings. Since these methods still create an instance of the class, you can also use other methods on the instances they create, such as `.add_topping()`:

```python
>>> a_pizza = Pizza.prosciutto()
>>> a_pizza
Pizza(['mozzarella', 'tomatoes', 'ham'])

>>> a_pizza.add_topping("garlic")
>>> a_pizza
Pizza(['mozzarella', 'tomatoes', 'ham', 'garlic'])
```

Python only allows one `.__init__()` method per class, but it’s possible to add as many alternative constructors as necessary by using class methods. This can make the interface for your classes self-documenting and simplify their usage.

So, when should you use class methods? In short, you should use class methods when you need to access and edit the data that’s tied to your class object rather than an instance of it. You can also use them to create alternative constructors for your class. **Use a class method when you need to access or modify class-level data or create factory methods that return class instances with specific configurations**.

### When to use Static Methods

You can use static methods when you need utility functions that don’t access or modify class or instance data, but where the functionality they provide still logically belongs within the class’s namespace.

Let’s stretch the pizza analogy even thinner, and add a static method that allows users to quickly fetch the diameter in inches based on common pizza sizes:
```python
class Pizza:
    # ...

    @staticmethod
    def get_size_in_inches(size):
        """Returns the diameter in inches for common pizza sizes."""
        size_map = {
            "small": 8,
            "medium": 12,
            "large": 16,
        }
        return size_map.get(size, "Unknown size")
```

The static method doesn’t have access to the instance or the class—and it doesn’t need that access. All that the method does is perform a dictionary lookup to return a number. You can call the static method both on a Pizza instance and the class itself:
```python
>>> from pizza import Pizza

>>> a_pizza = Pizza(["mozzarella", "tomatoes"])
>>> a_pizza.get_size_in_inches("medium")    # access by instance
12

>>> Pizza.get_size_in_inches("small")       # access by class
8
```

It’s purely for convenience and organizational purposes that static methods are part of the namespaces of the class and the instance. That convenience can be helpful because as a programmer-turned-pizza-baker, you may still sometimes need to look up how large a specific size of pizza should be. With .get_size_in_inches(), you can do that quickly.

So, when should you use static methods? **In short, you should use static methods when you need utility functionality that doesn’t need access to instance or class state or you should use static methods when you want to tie utility functionality related to your class right into its namespace**.

## Conclusion

By now, you’ve seen that instance, class, and static methods each play a distinct role in designing maintainable, object-oriented Python code. When you use them intentionally, these three method types can improve your code’s clarity, reusability, and testability.

- **Instance methods** encapsulate logic that operates on **individual objects**, giving you direct access to instance-specific state through `self`.
- **Class methods** focus on **class-level concerns**, providing an elegant way to create factory methods and alternative constructors through `cls`.
- **Static methods** act as **stand-alone utilities** that fit neatly within a class’s namespace.
- Choosing the right method type helps **communicate developer intent** by clarifying which data each method cares about.
- Using all three method types intentionally reduces bugs and improves maintainability by setting up **structured boundaries in class design**.

The next time you design a Python class, take a moment to consider whether your methods need access to instance data, class data, or neither. If it makes sense, then place a decorator before your method definition to make your code both more readable and more robust.
