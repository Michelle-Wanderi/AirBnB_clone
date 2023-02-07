![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
> AirBNB clone Console

![hbnb](./hbtn.png)

## About
This is the First Project towards our AirBnB clone project at [ALX](alxafrica.com). Done by [Michelle](https://github.com/Michelle-Wanderi) and [Ebenezer](https://github.com/Itsfoss0)


## General Use
Step 1. 
Clone the repository and cd into the repository

Step 2.
Inside the repository, there is a "console.py" file which contains the command line interpreter. Run this command in the terminal to see how it works
"$ python3 console.py"

Step 3.
When this command is run this appears
(hbnb)

Step 4.
Type ? to view all the commands in the interpreter


## Background Context 

[![AirBNB-clone](https://img.youtube.com/vi/XRH_8w1DEGI/0.jpg)](https://youtu.be/XRH_8w1DEGI "AirBNB clone")

### First step: Write a command interpreter to manage the AirBnB objects.

This is the first step towards building the first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called ```BaseModel```) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (```User```, ```State```, ```City```, ```Place```…) that inherit from ```BaseModel```
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

### What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Resources
__Read or watch__:
1. [cmd module](https://docs.python.org/3.8/library/cmd.html)
2. [cmd module in depth](http://pymotw.com/2/cmd/)
3. [uuid module](https://docs.python.org/3.8/library/uuid.html)
4. [datetime](https://docs.python.org/3.8/library/datetime.html)
5. [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
6. [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
7. [python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
8. [cmd module wiki page](https://wiki.python.org/moin/CmdModule)
9. [python unittests](https://realpython.com/python-testing/)


## Learning objectives
By the end of this project, you should be able to [explain to anyone](https://fs.blog/feynman-learning-technique/) without the help of __Google__

* [X] How to create a Python package
* [ ] How to create a command interpreter in Python using the cmd module
* [X] What is Unit testing and how to implement it in a large project
* [X] How to serialize and deserialize a Class
* [X] How to write and read a JSON file
* [X] How to manage datetime
* [X] What is an UUID
* [X] What is *args and how to use it
* [X] What is **kwargs and how to use it
* [X] How to handle named arguments in a function


## More info
The shell should look like this in interactive mode.

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
All tests should also pass in non-interactive mode:``` $ echo "python3 -m unittest discover tests" | bash```

![console](./console.png)

[![AirBNB-clone](https://img.youtube.com/vi/1mAC9x3aixE/0.jpg)](https://youtu.be/1mAC9x3aixE "AirBNB clone")