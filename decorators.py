# 1
import webbrowser
from app.example import *

def decorator(func):
    def inner():
        print("Hello")
        func()
        print("World")
    return inner

def name():
    print("You")


# 2
def decorator_example(func):
    def inner(a, b):
        print(f"Я почну множити число {a} на число {b}.")
        if b == 0 or a == 0:
            print("Неможливо зробити множення тому що число буде завжди 0.")
            return
        return func(a, b)
    return inner

# Practice

def web_decorator(func):
    def inner(url):
        if "https://" in url:
            return func(url)
        else:
            print("Incorrect url")
            return
    return inner



# func web
@web_decorator
def open_web_link(url):
    webbrowser.open(url)


# 2
@decorator_example
def multiply(a, b):
    print(a*b)

if __name__ == '__main__':
    # decorator_call = decorator(name)
    # print(decorator_call())
    # multiply(2, 5)
    #open_web_link("https://www.google.com")
    some_random_example()
    some_str_example(str(token_int))
