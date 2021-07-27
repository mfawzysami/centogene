# Centogene Tasks

## How to Install

The project is using miniconda as environment and package manager. we only use python=3.9 as a requirement but you can run it basically with any python 3.6+ 
No special packages required.

```shell script
$ conda env create -f requirements.yml
```

Afterwards, activate conda `centogene`

````shell script
$ conda activate centogene
````
## Task 1

## a) List 3 things you like about python and what do you dislike

### Things I like:

- Extremely easy syntax and few language keywords which makes 
python resembles natural human writing and/or pseudocode writing.
It is easy to translate any pseudocode into python code without much efforts.

- Massive community. Python has the largest developers community on the internet. 
This makes finding any python package that does highly specific tasks 
easily available in addition you can find any errors, bugs or exceptions clearly explained.
Besides, Python supports many numerical packages for data science, i.e. numpy, scipy, sikitlearn 
in addition to very mature charts and graph library like seaborn and matplotlib.

-  Python can fit in any software stack, whether we are designing web application, system application ,
GUI based application or even microservices or command line application. Python is there for you 
with the most up-to-date and state-of-the-art tools and libraries. Moreover,
Python runs nearly everywhere, you can run it on linux, mac, windows , android and even embedded systems using micropython.

### Things I dislike:

- Python is a scripting language which makes the code open to anyone has access 
to the server. I don't know of a method that can protect or obfuscate python code or
 convert it into binary code till now or at least didn't try it. On contrary to modern system programming languages like Golang 
 which supports both paradigms, being a script and in the same time you can cross compile the source code into a binary executable 
 to your target board or processor.
 
 - All python programs run under something called General Interpreter Lock (GIL) which really limits parallel and truely concurrent programming compared 
 to other languages like golang or rust...
 
 ## b) Which versioning system do you use
 
 Previously, I used centralized versioning systems like SVN and mercury but I have 
 been using (git - Decentralized Versioning system) for more than 10 years now for both Github, Gitlab and bitbucket....
 
 ## c) When you code, do you prefer object oriented or scripting style?
 
 It really depends on the project, for most bioinformatics related scripts, I prefer scripting style like defining methods and calling those methods.
 but for bigger projects with many layers of responsibilities, I prefer to use UML and Class Diagrams and model everything as objects with different behavior(s).
 Previously, I had been using "VisualParadigm" for Java Enterprise applications. But As far as web development in python is concerned, Django Design Pattern (MTV-MVC) 
 removes a lot of burden from us (developers) in organizing our code base. Things became more loose but controlled.
 
 ## d) What is the difference between static and class methods
 
 static methods are methods which don't have access to the class state where it is defined. It can not modify the class state. 
 We define static methods as auxiliary methods which perform highly specific recurrent functions related to the behavior of the encapsulating class
 but doesn't require access to the class state itself, for instance, decorator methods for performing authentication or authorization checking. 
 whereas, generally, class methods have access to the class state through its first parameter, I use 
 them specially in creating a factory design pattern. a general method which knows how to instantiate the encapsulating class, by performing 
 all the housekeeping operation required to successfully instantiate the class.
 
 ## e) Which IDE do you use?
 
 Pycharm professional Edition 2020.2, I purchased its pack license which includes Pycharm , Goland and Webstorm.
 
 ## f) How do you debug in python?
 
 Pycharm professional edition has an incredible interactive debugger for pure python as well as Django applications, Flask applications....
 
 Moreover, It has excellent python console with debugging enabled. you can write python code interactively on the console and attach a debugger session to that code,
 You can execute the python code and debug your code line by line or even a single function or method
  without the need to run the whole system or start the internal server if you are developing Django or Flask application(s).
 
 ## g) If you would do code review of another persons code, what are the major points you are looking at?
 
 Generally, I will look into this:
 
 - Presence of Code comments (Code Documentation) , decorating every method, function or class with appropriate simple short description of what 
 it does, what are the parameters, what should we expect from running that particular block.
 
 - proper naming convention, with snake style, I don't like camel-casing or pascal casing in python.
 
 - method names or function names should be short, concise and reflective of what the function/method does.
 
 - Proper use of exception handling.
 
 - Proper use of metadata typing in python 3.8+, by annotating parameters and return of functions which makes the code extremely easy and 
 remove the repeated use of "isinstance" keyword. Which I have been using too much just to get intellisense and code completion to the parameters of the method/function.
 
 - Presence of unit testing at least for vital sections of the core logic.
 
 
 
 ## Task 2:

To run it, simply execute 

```shell script
$ python task2.py --help
usage: task2.py [-h] --variants VARIANTS --diseases DISEASES [--out OUT]

Combining Variants with Disease Table

optional arguments:
  -h, --help            show this help message and exit
  --variants VARIANTS, -i VARIANTS
                        Absolute path of your variants Text File
  --diseases DISEASES, -d DISEASES
                        The absolute path of your diseases CSV File
  --out OUT, -o OUT     The absolute path of the combined output CSV file. Optional: Current working directory
```

```shell script
$ python task2.py --variants=variants.txt --diseases=disease_table.csv
```

## Task 3

To run it, simply execute

```shell script
$ python task3.py
``` 

### If both lists are much larger, would you change anything in your code?  
- I will use Pool from multiprocessing package and try to divide the upper list uniformly across the number of cores to speed up the iteration process
- anagrams list.append operation is a thread-safe operation, but I would usually use a locking mechanism like counter-based locking mechanism or more easily a queue 
data structure which is thread-safe for concurrent access, it became a habit or a programming style I usually take.


 
 
 
 
 