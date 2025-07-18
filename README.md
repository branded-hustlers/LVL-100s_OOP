Composition Over Inheritance

GROUP 5

ELENA NSAKIE

YAW BOACHIE



COMPOSITION OVER INHERITANCE: TOPIC SUMMARY

To understand composition over inheritance, we must first understand what inheritance is.

Inheritance is one of the four major pillars of Object-Oriented Programming (OOP).

Inheritance allows a subclass (“child class”) to inherit attributes and methods from a superclass (“parent class”). This means the child class can reuse and extend the functionality defined in the parent class.



Composition over inheritance is a design principle that prefers building classes by combining behaviours from multiple classes, rather than relying solely on a single parent class.

Composition over inheritance is preferred to inheritance because:

•	It makes the design more flexible.

•	It makes the design more modular.

•	It makes the design more reusable.



To be able to differentiate between composition over inheritance and inheritance clearly, let’s use a simple analogy to distinguish the two:

•	Inheritance is like a child raised by a single parent:

The child mimics or inherits the behaviour, habits, and values of that one parent.

•	Composition is like a child raised in a convent by multiple Roman sisters:

The child picks up behaviours, routines, and disciplines from multiple different, roman sisters not just one.



This analogy shows how:

•	In inheritance, a class is influenced by one parent.

•	In composition, a class is shaped by various smaller classes, each contributing specific functionality.



Our code implementation:

Our code was implemented in Python to demonstrate Composition over Inheritance. 

It models different types of devices (smartphone, yam phone, telephone, MiFi).

These models inherit various functionalities from not just one class, but different smaller, independent classes that provide specific features like calling, playing music, and connecting to the internet.

Running Code:

1\.	Create an object.

Elena\_smart\_phone = smart\_phone()



2\.	Call the method(function) of the class used to create the object.

Use\_smart\_phone()



The code runs...

