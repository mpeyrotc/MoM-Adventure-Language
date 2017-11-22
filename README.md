# MoM-Adventure-Language
The purpose of this project is to develop an Object-Oriented language to facilitate the creation of scenarios and components for the board game Mansions of Madness Second Edition. Through the use of this language, owners will have the opportunity  of creating additional content for the game and getting a bit into the field of computer programming. Therefore, a key emphasis of the language is to make it simple and comprehensible to promote its use and to give it more utility.

This repository comes with a compiler and virtual machine for the language. It requires [Python 3](https://www.python.org/) to run. This project was created as part of the Compiler Design course from Tec de Monterrey University for the Fall 2017 term. It was developed by:

* Marco A. Peyrot ([mpeyrotc.github.io](mpeyrot.github.io))
* Elias A. Mera ([a01280762@itesm.mx](mailto:a01280762@itesm.mx))

# User Manual 

This tutorial gives the user the necessary tools to make efficient use of the language and introduces all of the MoM-Adventure-Language features.

## Contents

1. File Structure
2. Classes
   1. Structure
   2. Inheritance
   3. Specifications
   4. Fields
   5. Constructors
   6. Methods
3. Specifications
   1. Purpose
   2. Structure
   3. Use
4. Enums
   1. Purpose
   2. Structure
   3. Use
5. Running a program
   1. Saving a file
   2. Running a program
   3. Considerations
6. Data types
7. Language Statements
   1. Input/Output
   2. if
   3. if else
   4. while
   5. Operations
8. Data Structures
   1. Arrays
   
# File Structure

A MoM-Adventure-Language file can consist of three types of structures: Classes explained in section 2, Specifications explained in section 3, and Enums explained insection 4. These can be located at any point of the file, but __cannot be nested within each other__. Another language constraint is that these elements must always be defined before they are used, because it is processed by a one pass compiler.

In order for a file program to compile, there must be at least one class present in the file and it must have defined a main method, which is the main entry point of any program made with this language. The main method must always have this structure:

```java
Nothing main() {
   ...
};
```

# Classes

Classes are the heart of the MoM-Adventure-Language. They are structures designed to represent an abstraction from the real world. In our case, a game component from Mansions of Madness, but it can be used as a genral purpose language too.

## Structure

A MoM class is defined according to the following syntax:

```java
class ClassName is_a Component of_type SpecName,  OtherSpec {
   field<Type> fieldName;
   ...
   
   ClassName() {
      ...
   };
   
   ReturnType methodName(Type argument, ... , Type anotherArgument) {
      ...
      return someValue;
   };
   
   Nothing methodName() {
      ...
   };
   ...
};
```
There are several things to consider with this example. First, notice that class names have to start with an uppercase letter and must always specify their parent. 

## Inheritance
The base class of all classes is the Component class, which is internally defined. The language only supports single-inheritance, so only one parent constructor is allowed.

When instantiating an object of a certain class, its constructor is called, when called, it immediately calls its parent's constructor and the process continues until the Component class constructor gets called. As a result, initializations are applied from in a top-bottom fashion.

## Specifications

After specifying the constructor, the user can declare which specifications a particular class implements. Implementing an interface makes that class of the same type of the specification; it could be considered a simpler form of multi-inheritance as will be seen later. It is important to remember that __this part is entirely optional__.

## Fields

After the first line of the class, come the class fields. These are the global variables of any class instance. The language does not support _static_ members, so these are unique to each class instance. As with specifications, these are too entirely optional. 

There are 3 types of variables that can be fields: primitives, object references, and arrays of the latter types. These must be declared between the < and > symbols.

## Constructor

After this comes the constructor which is mandatory and must follow these specifications:

1. It has to have the same name as the class and must not have a return type or arguments.
2. It cannot declare variables inside its body.
3. It should only be used to initialize global variables (fields).
4. It can be left empty.

## Methods

Finally come the methods, which are only requiered to be uniquely named. The scope of this restriction applies to the ancestor's methods too. Their structure is similar to that of the constructor, but with some key differences:

1. The return type must always be specified and it can only be primitive (See section 6).
2. Its name must always start with a lowercase letter and continue using the camelCase rule.
3. It may have or not, arguments, these must follow the next structure:

```java
Type name, Type name, ... , Type Name
```

4. Methods in MoM can receive both primitive and object arguments. However, array arguments are not suported.
5. If the return type is `Nothing` the method should not have a `return` with a value after it.
6. If the return type is different from `Nothing` it is mandatory to have a `return` statement at every posible execution branch. Notice that this is not enforced by the compiler.
