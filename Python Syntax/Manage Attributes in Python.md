# Getters and Setters: Manage Attributes in Python
[[_TOC_]]


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
