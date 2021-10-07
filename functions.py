# Only one way to write functions yay! NO MORE ARROW FUNCTIONS!!
# def keyword -> DEFINE a function
# def functionName(parameters):
def greeting():
    # code block
    print('Hello World')

# Naming Conventions for a Python function:
#   - start with letter or underscore
#   - alphanumeric chars and underscores
#   - lowercase
#   - can not be a reserved keyword in Python

# Stubbing a function -> define function and write code inside later
# must use pass keyword or SyntaxError
# placeholder that does nothing
greeting()

def greeting():
    # can not leave this empty
    pass

# argument = bits of data you pass in, 
# parameter = names function uses to understand data that was passed into it
# function with one parameter
def greeting(name):
    print('Goodbye', name)

greeting('Erin')
greeting('Paolo')
# greeting() -> causes error even when defines earlier

# NOTES: seems like in python you must declare the function first to be able to call it
# no method overloading in python .. is there method overriding?


