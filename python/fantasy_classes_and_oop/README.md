### Classes and Object-Oriented Programming

This project exhibits the fundamentals of object-oriented design.

- **Encapsulation**: This project does not exhibit encapsulation as every property and method are public (_not good_). To fix this, I would have to add getters and setters.
- **Abstraction**: The classes in this project are neatly abstracted. Each method hides internal functionality well enough. 
- **Inheritance**: The purpose of this project was to understand inheritance. Archetypes like Warrior and Sorceress inherit from the Hero class. Spells like Sleep and Heal inherit from the Magic class.
- **Polymorphism**: One example of polymorphism can be found in the Sorceress's _cast_ method. Rather than creating a cast method for each of the different spells, one method works for any given spell. 

Some inconsistencies exist in this project. For example, the Knight class has a Heal spell, but no way to cast it. If I wanted to expand upon this, I would abstract the Sorceress's _cast_ method to the Hero class. That way, any child of Hero could cast spells. I would also apply encapsulation by making properties and methods private or protected where appropriate and by adding getters and setters.  