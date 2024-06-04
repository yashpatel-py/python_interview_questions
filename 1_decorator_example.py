# Question: what is decorator in python?
# Answer: A decorator is a function that modifies the behavour of another function.

# Example
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()