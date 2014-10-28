Title: Code: A Non-Programmers Journey Into a World of Turning Machines
Date: 10-27-2014
Category: Programming
Status: Draft
Slug: code
Tags: Life, Learning, Articles, Python

> "Talk is Cheap. Show me the Code"

> \- Linus Torvalds (Linux Kernel Mailing List)

## Some History

It was 2012, even before [President Obama's](http://code.org) initiative to address the importance of programming literacy to the american public, I was facing a similar dilemma in my own life.

I had recently graduated with a degree in Chemistry, and spent all of college preparing for a future as a Doctor.

The only programs I've ever written at the time were simple shell scripts that automated some simple routines.

## Learning to Reinvent

Every day you reinvent yourself. You’re always in motion.

> But you decide every day: __forward or backward__.

It’s okay to get disillusioned. That’s what failure is about. Success is better than failure but the biggest lessons are found in failure.

> Very important: There’s no rush.

Spend time every day coding. No matter how small or simple the application.

Try to automate anything you can, anything where programming can help.

Slowly you'll find your skills developing and being enriched.

## Quantify Your Progress

### Goals (2013-2014)
- Find a programming mentor
- Learn 2 new programming languages
- Read one technical book a month
- Write over 10k lines of code.
- Attend a Hackathon
- Read the entire standard library for 1 language.
- Complete 1 Open Source Project
- Contribute to an open source project
- Create my own set of build tools
- Start a programming blog

### This Year (2014-2015)
- Find a mentee
- Master 1 language
- Build and release a mobile app
- Become a contributor to a software project
- Maintain a library of modules or do a rewrite of an existing library/module
- Competative programming
- Build a compiler

## Start Building Things

Whenever you start pursuing something, __make sure to keep copy/pasting to a minimum__ also use the core language primitives without depending on code from an outside library.

> If you want to get the most out of the experience, build off the skills and tools you have now in earnest.

At the end of every project, perform a postmortem to characterize and conclude how things went. Make sure to specify things like, what went well and what could have been better.

> You'll find every skill and tool will be enriched from this exercise. You'll have also have gained some new ones as well.

### Here are a couple project ideas.

Build a __simple command line application__ that follows POSIX standard and API's.
Make it composable with other tools. Always consider modularity and keep in mind all the possible applications and interfaces, make sure to work those into your design.

### A File Rename/Move/Copy/Symlink tool.
* You'll need to efficiently traverse the directory tree.
* Are you going to do it recursively?
* Do you match with regular expressions, or do you use other facilities of your language runtime to handle it?
* Create a distinct __separation of concerns__ between program components.
	* For instance, you don't want to couple your FileIO while you're traversing the directory.

### A Parser
* A parser that will read some data and outputs it in another format.
* It doesn't need to be a text file. It could even be a program that grabs the ID3 tags from mp3 files.
* Learn about all the ways text can be represented/encoded.
	* What text can be represented using 7-bit vs 8-bit ASCII.
	* Whats the difference between Unicode and UTF-8. How are invisible characters like tabs, newlines, and null terminators represented.
* Know where all these types of encoding schemes exist and be able to make the right assumptions.

### A logging program for taking notes.
* Learn about how filesystem io, streams/buffers, and file descriptors work. Figure out what the best format/standard to use.
* What kind of notations will you use for formatting and markup?
	* How will you store and generate output? TXT, CSV, JSON or even a SQLite database.
	* You could even have it interchange between multiple formats and create a schema that ensures data isn't lost between conversions.

### A smart todo list or task management tool.
* Take into consideration that tasks can range in priority and are also sensitive to time of day/place.
* Also some tasks need to be done in a particular order.
* Determine the most efficient way to structure your data.
* Learn the argument parsing library for your language/runtime and design appropriately.

### Plug and Play Philosophy
The Unix philosophy is one of building small tools that do one thing well over large monolithic applications and frameworks. This becomes powerful once you start combining other tools together to perform more complex task.

Although this may sound simple, in practice it takes a lot of time and polish to get programs to work at this level. For examples consider you want to use the batch file rename tool and ID3 tag parser to manage your music collection. If you've built them correctly, these two tools which originally knew nothing of the other should compose seamlessly through the interface of Unix pipes and streams. If the solution is writing to a file that the user modifies, or only runs correctly on certain platforms configured a certain way are indicators that design has been compromised for the sake of utility or time.

## Language Doesn't Matter

Todo:

## Onward

Here is a small list I came up with to consolidate my progress.

### Data Structures

- Linear Data Structures (Lists, LIFO/FIFO)
- Numerical Algorithms
- Hashing / Indexing
- Trees (BST, AST, Heaps etc…)
- Abstract Data Structures (Priority Queues)
- Tries / Advanced Data Structures

### Algorithms

- Basic Sorts Algorithms
- Recursive Algorithms
- Data Structure Traversals (BFS, DFS, Trees etc…)
- Graphs Search / Network Programming
- Huffman Encoding / Compression Algorithms
- String / Numerical Computation
- Encryption / Cryptography

### System Level

- Understanding Networks/Protocols/Socket Programming
- Complexity / NP Type Problems
- User Space vs Kernel Spaceco
-  Concurrency Models (Threads, Events, Coroutines etc...)
	-  Synchronization Primitives
	- IO vs CPU Bound
- Compilation, Linking, Interpretation
	-  JITs, AOT, IR
- Pointers/Indirection vs Abstraction
- Memory Addressing / Garbage Collection
- State Machines
- Scope Lexical vs Block

### OOP and Design

- Understanding Inheritence, Encapsulation and Polymorphism
- Method Dispatch Compiletime vs Runtime
-  Static / Passive Code Generation
- Metaprogramming / Code Decoupling
- OOP Design Patterns
	- Singletons
	- AbstractFacory
	- Prototype
	- Adaptor
	- Proxy
	- Bridge
	- Observe
	- Visitor
	- MVP

### Application Programming

- Understands GUI Tookits
- Write Self Documentation and Normal Documentation
- Testing
- Continuous Integration
- Knows the way of CLI and shell automation

### Computer Science Theory

- Space vs Time Tradeoffs
- Recursion
- Self hosting / Bootstrapping Compilers
- Atomicy / Fault Tolerance
- Computability Theory / Turing Machines
- Boolean Algebra
- Type Theory / Lambda Calculus

### Attitude

- Short Term Pessimist, Long term Optimist.
- Multiple Refactoring, iterative programming.
- Engineer a solution but doesn't optimize prematurely.
- Structure based on good design principles.
- Multiple backup schemes, makes a habit of using VCS.
- Project Post-Mortems are necessity.
- Always trying to to build and sharpen personal toolkit.
- Managing complexity
    - Knows where to generalize abstractions decouple using indirection.

### Languages (One of each)

- Low Level (Assembly, C, Lisps)
- High Level OOP (Java, C++, C#)
- Interpreted/Scripting (Python, JS, Shell, Perl)
- Declarative (SQL, RegEX)
- Functional/Other (Scheme, Haskell, DSLs)_
- Application Languages (Mobile, [HT]ML, Web,  APIs/Frameworks)