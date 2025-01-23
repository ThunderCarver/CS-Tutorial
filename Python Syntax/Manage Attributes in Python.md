# Getters and Setters: Manage Attributes in Python
* [Getting to Know Getter and Setter Methods](#getting-to-know-getter-and-setter-methods)
  * [What Are Getter and Setter Methods?](#what-are-getter-and-setter-methods)
  * [Where Do Getter and Setter Methods Come From?](#where-do-getter-and-setter-methods-come-from)
* [Using Properties Instead of Getters and Setters: The Python Way]()
* [Conclusion](#conclusion)


Getter and setter methods allow you to access and mutate non-public attributes while maintaining encapsulation. 
In Python, you’ll typically expose attributes as part of your public API and use properties when you need attributes with functional behavior. 
This tutorial guides you through writing getter and setter methods, replacing them with properties, and exploring alternatives like descriptors 
for optimized attribute management.

By the end of this tutorial, you’ll understand that:

- **Getter** and **setter** methods allow you to access and modify data attributes while maintaining **encapsulation**.
- **Python properties** can replace getters and setters, providing a more Pythonic way to manage attributes with **functional behavior**.
- You typically **avoid** using getters and setters in Python unless necessary, as **properties** and **descriptors** offer more flexible solutions.
- **Descriptors** are an advanced Python feature that enable reusable attributes with **attached behaviors** across different classes.
- In some scenarios, **inheritance** limitations may make traditional getters and setters preferable over properties.

Even though properties are the Pythonic way to go, they can have some practical drawbacks. Because of this, you’ll find some situations 
where getters and setters are preferable over properties. This tutorial will delve into the nuances(细微差别) of using different approaches, equipping 
you with the knowledge to make informed decisions about attribute management in your classes.

To get the most out of this tutorial, you should be familiar with Python [object-oriented programming](https://realpython.com/python3-object-oriented-programming/). It’ll also be a plus if you 
have basic knowledge of Python [properties](https://realpython.com/python-property/) and [descriptors](https://realpython.com/python-descriptors/).

## Getting to Know Getter and Setter Methods
When you define a class in object-oriented programming (OOP), you’ll likely end up with some instance and class attributes. 
These attributes are just variables that you can access through the instance, the class, or both.

Attributes hold the internal state of objects. In many cases, you’ll need to access and mutate this state, which involves 
accessing and mutating the attributes. Typically, you’ll have at least two ways to access and mutate attributes. You can either:

1. Access and mutate the attribute directly
2. Use methods to access and mutate the attribute

If you expose the attributes of a class to your users, then those attributes automatically become part of the class’s public API. 
They’ll be **public attributes**, which means that your users will directly access and mutate the attributes in their code.

Having an attribute that’s part of a class’s API will become a problem if you need to change the internal implementation of the attribute itself. A clear example of this issue is when you want to turn a stored attribute into a computed one. A stored attribute will immediately respond to access and mutation operations by just retrieving and storing data, while a computed attribute will run computations before such operations.

The problem with regular attributes is that they can’t have an internal implementation because they’re just variables. So, changing an attribute’s internal implementation will require converting the attribute into a method, which will probably break your users’ code. Why? Because they’ll have to change attribute access and mutation operations into method calls throughout their codebase if they want the code to continue working.

To deal with this kind of issue, some programming languages, like Java and C++, require you to provide methods for manipulating the attributes of your classes. These methods are commonly known as getter and setter methods. You can also find them referred to as accessor and mutator methods.

### What Are Getter and Setter Methods?
Getter and setter methods are quite popular in many object-oriented programming languages. So, it’s pretty likely that you’ve heard about them already. As a rough definition, you can say that getters and setters are:

Getter: A method that allows you to access an attribute in a given class
Setter: A method that allows you to set or mutate the value of an attribute in a class

In OOP, the getter and setter pattern suggests that public attributes should be used only when you’re sure that no one will ever need to attach behavior to them. If an attribute is likely to change its internal implementation, then you should use getter and setter methods.

Implementing the getter and setter pattern requires:
1. Making your attributes non-public
2. Writing getter and setter methods for each attribute

For example, say that you need to write a Label class with text and font attributes. If you were to use getter and setter methods to manage these attributes, then you’d write the class like in the following code:
```python
class Label:
    def __init__(self, text, font):
        self._text = text
        self._font = font

    def get_text(self):
        return self._text

    def set_text(self, value):
        self._text = value

    def get_font(self):
        return self._font

    def set_font(self, value):
        self._font = value
```
In this example, the constructor of Label takes two arguments, text and font. These arguments are stored in the ._text and ._font non-public instance attributes, respectively.

Then you define getter and setter methods for both attributes. Typically, getter methods return the target attribute’s value, while setter methods take a new value and assign it to the underlying attribute.

<blockquote>Note: Python doesn’t have the notion of access modifiers, such as private, protected, and public, to restrict access to attributes and methods in a class. In Python, the distinction is between public and non-public class members.<br>
If you want to signal that a given attribute or method is non-public, then you should use the well-established Python convention of prefixing the name with an underscore (_).<br>
Note that this is just a convention. It doesn’t stop you and other programmers from accessing the attributes using dot notation, as in obj._attr. However, it’s bad practice to violate this convention.<br>    
</blockquote>

### Where Do Getter and Setter Methods Come From?
To understand where getter and setter methods come from, get back to the Label example and say that you want to automatically store the label’s text in uppercase letters. Unfortunately, you can’t simply add this behavior to a regular attribute like .text. You can only add behavior through methods, but converting a public attribute into a method will introduce a **breaking change** in your API.

So, what can you do? Well, in Python, you’ll most likely use a property, as you’ll learn soon. However, programming languages like Java and C++ don’t support property-like constructs, or their properties aren’t quite like Python properties.

That’s why these languages encourage you never to expose your attributes as part of your public APIs. Instead, you must provide getter and setter methods, which offer a quick way to change the internal implementation of your attributes without changing your public API.

Encapsulation is another fundamental topic related to the origin of getter and setter methods. Essentially, this principle refers to bundling data with the methods that operate on that data. This way, access and mutation operations will be done through methods exclusively.

The principle also has to do with restricting direct access to an object’s attributes, which will prevent exposing implementation details or violating state invariance.

To provide Label with the newly required functionality in Java or C++, you must use getter and setter methods from the beginning. How can you apply the getter and setter pattern to solve the problem in Python?

Consider the following version of Label:
```python
class Label:
    def __init__(self, text, font):
        self.set_text(text)
        self.font = font

    def get_text(self):
        return self._text

    def set_text(self, value):
        self._text = value.upper()  # Attached behavior
```
In this updated version of Label, you provide getter and setter methods for the label’s text. The attribute holding the text is non-public because it has a leading underscore on its name, ._text. The setter method does the input transformation, converting the text into uppercase letters.

Now you can use your Label class like in the following code snippet:
```python
>>> from label import Label

>>> label = Label("Fruits", "JetBrains Mono NL")
>>> label.get_text()
'FRUITS'

>>> label.set_text("Vegetables")
>>> label.get_text()
'VEGETABLES'
```
Cool! You’ve successfully added the required behavior to your label’s text attribute. Now your setter method has a true goal instead of just assigning a new value to the target attribute. It has the goal of adding extra behavior to the ._text attribute.

Even though the getter and setter pattern is quite common in other programming languages, that’s not the case in Python.

Adding getter and setter methods to your classes can considerably increase the number of lines in your code. Getters and setters also follow a repetitive and boring pattern that’ll require extra time to complete. This pattern can be error-prone and tedious. You’ll also find that the immediate functionality gained from all this additional code is often zero.

All this sounds like something that Python developers wouldn’t want to do in their code. In Python, you’ll probably write the Label class like in the following snippet:
```python
>>> class Label:
...     def __init__(self, text, font):
...         self.text = text
...         self.font = font
...
```
Here, .text, and .font are public attributes and are exposed as part of the class’s API. This means that your users can and will change their value whenever they like:
```python
>>> label = Label("Fruits", "JetBrains Mono NL")
>>> label.text
'Fruits'

>>> # Later...
>>> label.text = "Vegetables"
>>> label.text
'Vegetables'
```
Exposing attributes like .text and .font is common practice in Python. So, your users will directly access and mutate this kind of attribute in their code.

Making your attributes public, like in the above example, is a common practice in Python. In these cases, switching to getters and setters will introduce breaking changes. So, how do you deal with situations that require adding behavior to your attributes? The Pythonic way to do this is to replace attributes with properties.

## Using Properties Instead of Getters and Setters: The Python Way
The Pythonic way to attach behavior to an attribute is to turn the attribute itself into a property. Properties pack together methods for getting, setting, deleting, and documenting the underlying data. Therefore, properties are special attributes with additional behavior.

You can use properties in the same way that you use regular attributes. When you access a property, its attached getter method is automatically called. Likewise, when you mutate the property, its setter method gets called. This behavior provides the means to attach functionality to your attributes without introducing breaking changes in your code’s API.

As an example of how properties can help you attach behavior to attributes, say that you need an Employee class as part of an employee management system. You start with the following bare-bones implementation:
```python
class Employee:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    # Implementation...
```
This class’s constructor takes two arguments, the name and date of birth of the employee at hand. These attributes are directly stored in two instance attributes, .name and .birth_date.

You can start using the class right away:
```python
>>> from employee import Employee

>>> john = Employee("John", "2001-02-07")

>>> john.name
'John'
>>> john.birth_date
'2001-02-07'

>>> john.name = "John Doe"
>>> john.name
'John Doe'
```
Employee allows you to create instances that give you direct access to the associated name and birth date. Note that you can also mutate the attributes by using direct assignments.

As your project evolves, you have new requirements. You need to store the employee’s name in uppercase letters and turn the birth date into a date object. To meet these requirements without breaking your API with getter and setter methods for .name and .birth_date, you can use properties:
```python
from datetime import date

class Employee:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = date.fromisoformat(value)
```
In this enhanced version of Employee, you turn .name and .birth_date into properties using the @property decorator. Now each attribute has a getter and a setter method named after the attribute itself. Note that the setter of .name turns the input name into uppercase letters. Similarly, the setter of .birth_date automatically converts the input date into a date object for you.

As mentioned before, a neat feature of properties is that you can use them as regular attributes:
```python
>>> from employee import Employee

>>> john = Employee("John", "2001-02-07")

>>> john.name
'JOHN'

>>> john.birth_date
datetime.date(2001, 2, 7)

>>> john.name = "John Doe"
>>> john.name
'JOHN DOE'
```
Cool! You’ve added behavior to the .name and .birth_date attributes without affecting your class’s API. With properties, you’ve gained the ability to refer to these attributes as you would to regular attributes. Behind the scenes, Python takes care of running the appropriate methods for you.

You must avoid breaking your user’s code by introducing changes in your APIs. Python’s @property decorator is the Pythonic way to do that. Properties are officially recommended in PEP 8 as the right way to deal with attributes that need functional behavior:
<blockquote>For simple public data attributes, it’s best to expose just the attribute name, without complicated accessor/mutator methods. Keep in mind that Python provides an easy path to future enhancement, should you find that a simple data attribute needs to grow functional behavior. In that case, use properties to hide functional implementation behind simple data attribute access syntax. [Source](https://peps.python.org/pep-0008/#designing-for-inheritance)</blockquote>

Python’s properties have a lot of potential use cases. For example, you can use properties to create read-only, read-write, and write-only attributes in an elegant and straightforward manner. Properties allow you to delete and document the underlying attributes and more. More importantly, properties allow you to make regular attributes behave like managed attributes with attached behavior without changing the way you work with them.

Because of properties, Python developers tend to design their classes’ APIs using a few guidelines:

* Use **public attributes** whenever appropriate, even if you expect the attribute to require functional behavior in the future.
* **Avoid** defining **setter** and **getter** methods for your attributes. You can always turn them into properties if needed.
* Use **properties** when you need to **attach behavior** to attributes and keep using them as regular attributes in your code.
* **Avoid side effects** in properties because no one would expect operations like assignments to cause any side effects.

Python’s properties are cool! Because of that, people tend to overuse them. In general, you should only use properties when you need to add extra processing on top of a specific attribute. Turning all your attributes into properties will be a waste of your time. It may also imply performance and maintainability issues.

## Conclusion
Now you know what getter and setter methods are and where they come from. These methods allow access and mutation of attributes 
while avoiding API changes. However, they’re not so popular in Python because of the existence of properties. Properties allow 
you to add behavior to your attributes while avoiding breaking changes in your APIs.

Even though properties are the Pythonic way to replace traditional getters and setters, properties can have some practical drawbacks
that you can overcome with getters and setters.

**In this tutorial, you’ve learned how to**:

- [ ] Write getter and setter methods in Python
- [ ] Use Python properties to replace getter and setter methods
- [ ] Use Python tools, like descriptors, to replace getters and setters
- [ ] Decide on when setter and getter methods can be the right tool for the job
- [ ] With all this knowledge, you can now decide when to use either getter and setter methods or properties in your Python classes.
