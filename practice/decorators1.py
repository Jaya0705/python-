def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")
print('hi')
say_whee = my_decorator(say_whee)





from datetime import datetime
def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            print("day time")
            func()
        else:
            print("night time")
            pass  
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)






def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

@do_twice
def say_whee():
    print("Whee!")






def hello_decorator(func): 
    def inner1(*args, **kwargs): 
          
        print("before Execution") 
        returned_value = func(*args, **kwargs) 
        print("after Execution")  
        return returned_value 
          
    return inner1 
  
  
@hello_decorator
def sum_two_numbers(a, b): 
    print("Inside the function") 
    return a + b 
print sum_two_numbers(1, 2)

