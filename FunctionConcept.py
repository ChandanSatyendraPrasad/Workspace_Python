# Global Scope

greeting = "Hi"

def say_hello():
    print(greeting + " from inside the function")
    
say_hello()
print(greeting + " from outside the function")

def input_and_print():
    num = int(input("Enter a number: "))
    print(num)

input_and_print()

# Local Scope
def greet():
    message = "Hello World"
    print(message)
    
greet()
#print(message)

# Parameter Scope
def greetee(name):
    message = "Hello " + name
    print(message)

name = input("Enter your name: ")
greetee(name)