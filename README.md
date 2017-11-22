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
   1. Special classes
7. Language Statements
   1. Input/Output
   2. if
   3. if else
   4. while
   5. Operations
8. Data Structures
   1. Arrays
9. Real World Example
   
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

# Specifications

Specifications are much like [Java Interfaces](https://docs.oracle.com/javase/tutorial/java/concepts/interface.html), and are a key feature of the MoM language.

## Purpose

A Specification is used to define a set of methods that are relevant to a specific type. For example, we could have a Monster Specification that establishes that Monster types have to have the methods attack, and defend as shown below:

```java
specification Monster {
   Int attack();
   Nothing defend(Int value);
};
```

## Structure

Specifications, as classes, hare identified with a name that starts with an uppercase letter. They do not define the implementation of the methods they expose, they only specify the signature of the methods. There is no specification inheritance.

## Use

A class is just a user defined type, specifications let these classes have more than one type by conforming themselves to the specification's requirements. These requirements involve two things:

1. Add the spacification to the list of specifications implemented by the class by putting its name after the `of_type` keyword in the class definition.
2. Implement all the methods defined by the specification. If this is not done, a compilation error will occur.

Name conflicts between interfaces are not validated at compile time and could lead to errors if their arguments differ from one another.

Example:

```java
class Witch is_a Component of_type Monster {
   Witch() {
      ...
   };
   
   ...
   
   Int attack() {
      ...
      return attackValue;
   };
   
   Nothing defend(Int value){
      ...
   };
   
   ...
};
```

Because the Witch class implements the Monster specification, it can me added to the monster array for example,

```java
Monster[10] monsters;
monster[0] = new Witch();
```

which adds a lot of flexibility and power to the language.

# Enumerations

Enumerations are simpler and more elegant way of using [_magic numbers_](https://en.wikipedia.org/wiki/Magic_number_(programming)) in MoM code. They are entirely based on C enums, therefore they are equivalent to integers and can be used in any expressions that supports integer values. Enumerations are defined as follows:

```java
enumerate NameOfEnum {
   VALUEA, VALUEB, VALUEC, ...;
};
```

## Purpose

When the code is glittered with a bunch of numbers, it is often difficult to rememeber the purpose they have in the code or what they represent. Enumerations give names to integers. However, the values given to the names defined in an enumeration are automatically assigned. There is no guarantee about what the value of a enumeration might be, so make sure to not make code that depends on the specific value of an enumeration element.

## Structure

As seen in the example above, enumerations are identified by a name that starts with a capital letter (in the same fashion as classes and specifications). The values contained within the collection __must__ be all in uppercase and separated by commas.

## Use

A classic use of the enumerations in programming languages is the use enumerable elements like cards, days of the week or months. In MoM we could define a `Days` enumeration and use it in our code as as shown below:

```java
enumerate Days {
    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY;
};
```

inside a method...

```java
...
Int day = ...
if(day == Days.MONDAY) {
   ...
} else {
   if(day == Days.TUESDAY) {
      ...
   } else {
      ...
   };
};
...
```

# Running a program

A MoM program is typically run from the terminal using the Python 3 interpreter. As of today, the MoM language only supports input and output from the console.

## Saving a file

A MoM program is contained in a text file that must end with the __.mom__ extension. No other restrictions apply.

## Running a program

Locate the file to be run, in our case __test.mom__, and put it in the directoy you want. For simplicity, we will move the file to the same place as the Main.py file is. Run the following command to compile and execute:

```shell
$ python3 Main.py test.mom

printed something out with execution...

$
```
## Considerations

A temporal file called __temp.mom__ is created to store intermediate code. This file is then run by the virtual machine provided with the language. As a result, please avoid naming your programs as __temp.mom__.

# Data types

TThe language comes with four basic primitive types and a special type which represents the `void` keyword in the C programming language, these are: 

* Text : represents a sequence of characters. It is the name for the string type in languages like Java and C.
* Int : represents an integer number.
* Real : represents a real number. More specifically, the double or float types common
to C-like languages.
* Boolean : represents the conditional values TRUE and FALSE.
* Nothing : represents no return value, equivalent to the void type in C-like languages.

(please refer to documentation to see which types are compatible with each other and by what operations).

## Special classes

In addition to the creative liberty the language provides to the user, it will provide some classes by default. These classes will serve as the base for further development and aid the programmer to start making as soon as possible new stories and scenarios for the game. As the user of the language gains more experience, he/she will be able to develop new game mechanics, rules, or physical components through more complicated programs and objects. As a result, the language should be able to support the creation of any type of text-based game.

* Component: this is the base class for the MoM Adventure Language. It represents a game component (like a card, mat, or token). All other objects in the language inherit from this class. Its fields are width and height.
* Face: represents the side of a component. It is a container for several sections.
* Card: represents a physical game card, it has two faces and each one is divided into
sections such as title, image, description, cost, etc..
* Token: represents a physical game token or carton piece.
* Message: it is a simple container that comes with a title, message, and two types of input: via a numeric or text entry, or a series of options which the player can select.
* Player: it is a special instance of component since it can have several other compo- nents attached. Its base members and fields are those found on the player sheet in the real board game.
* Creature: it is a kind of special component since it has several additional actions related to it. These actions are move, attack, and evade.

# Language Statements

This section presents the different structures and statements supported by the language.

## Input/Output

The language provides two functions for output, one writes over the same line (`Write`), while the other appends a _newline_ character at the end of its argument (`WriteLine`).

* `Write`: this special function is used to print into the standard output a stream of characters which are not followed by a default newline character.

```java
Nothing Write(Text text); 
Nothing Write(Int number); 
Nothing Write(Real number);
Nothing Write(Boolean value); 
Nothing Write();
```

* `WriteLine`: this special function does the same as the adds the newline character at the end of the stream. It has two versions, one with arguments and one without.

```java
Nothing WriteLine(Text text); 
Nothing WriteLine(Int number);
Nothing WriteLine(Real number); 
Nothing WriteLine(Boolean value); 
Nothing WriteLine();
```

There are also default methods to get input from the user, these are:

* `ReadText`: this function reads from the standard input a stream of characters and stores them in a Text variable.

```java
Nothing ReadText(Text variable);
```

* `ReadInt`: this function reads from the standard input a stream of numeric characters and stores them in an Int variable.

```java
Nothing ReadInt(Int variable);
```

* `ReadReal`: this function reads from the standard input a stream of numeric charac- ters (and the ‘.’ character) and stores them in a Real variable.

```java
Nothing ReadReal(Real variable);
```

* `ReadBoolean`: this function reads from the standard input a stream of alphanumeric characters that form the words True or False and stores them in a Boolean variable.

```java
Nothing ReadBoolean(Boolean variable);
```

The input functions store the value they receive in the variable passed as an argument.

## if

`if` statements are the same as any other imperative programming language:

```java
if(condition) {
   ...
};
```

## if else

The same occurs with the `if else` statement:

```java
if(condition) {
   ...
} else {

};
```

## while

The language supports just one kind of loop, the while statement.

```java
while(condition) {
   ...
};
```

## Operations

The MoM language supports the unary operators `+` `-` and `!` (not) and the binary operators `+`, `-`, `*` (times) and `/` (divides) for arithmetic operations. There are also relational operators like `<`, `<=`, `>`, `>=`, and `==`. Finally, users can also make use of the logical operators `&&` (and) and `||` (or).

# Data Structures

The language comes with just one type of structuref or multidimensional type: the array. 

## Arrays

This structure can contain arguments of any type that is not also an array.It can be used anywhere inside the code, except as a function argument.

To declare an array (which can have any number of dimensions) you must specify its max size, because this value will not change during the whole program execution:

```java
Type[dimensionA][dimensionB]...; 
```

dimensions can only be integer values.

To use it, just specify the index values for each dimension. If the array indeces are out of range, an error occurs. For example:

```java
arrS[i + 1] = arrS[hi];
```

where `i` and `hi` are integers.

# Real World Example

This section presents a working implementation of Quick Sort done in the MoM language.

```java
class Math is_a Component {
    field<Int[10]> arrS;

    Math() {

    };

    Int partition(Int lo, Int hi){
        Int pivot = arrS[hi];
        Int i = (lo - 1);
        Int j = lo;
        Int temp = 0;
        while(j < hi){
            if(arrS[j] <= pivot){
                i = i + 1;
                temp = arrS[i];
                arrS[i] = arrS[j];
                arrS[j] = temp;
            };
            j = j + 1;
        };
        temp = arrS[i + 1];
        arrS[i + 1] = arrS[hi];
        arrS[hi] = temp;
        return i + 1;
    };

    Nothing sortArrS(Int lo, Int hi){
        if(lo < hi){
            Int pi = partition(lo, hi);
            sortArrS(lo, pi - 1);
            sortArrS(pi + 1, hi);
        };
    };

    Nothing main(){
        arrS[0] = 34;
        arrS[1] = 0;
        arrS[2] = 10;
        arrS[3] = 4;
        arrS[4] = 12;
        arrS[5] = 0;
        arrS[6] = 99;
        arrS[7] = 48;
        arrS[8] = 1;
        arrS[9] = 28;

        Int i = 0;
        WriteLine("Unsorted array:");
        while(i < 10){
            Write(arrS[i]);
            Write(" ");
            i = i + 1;
        };
        WriteLine(" ");
        sortArrS(0, 9);
        WriteLine("Sorted array: ");
        i = 0;
        while(i < 10){
            Write(arrS[i]);
            Write(" ");
            i = i + 1;
        };
        WriteLine(" ");
    };
};
```

For more information, please visit the tutorial video.

<a href="https://www.youtube.com/watch?v=9TGBTczCE54&feature=youtu.be" target="_blank">
   <img src="https://www.youtube.com/watch?v=9TGBTczCE54&feature=youtu.be/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>
