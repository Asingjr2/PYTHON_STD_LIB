"""Creates base class for use with functools."""
from functools import wraps


def print_through_functools(f):
    """Creates function wrapper that will return itself of implement 
    another function if exclude is None."""
    @wraps(f)
    def function_wrapper(*args, **kwargs):
        if kwargs.get('exclude'):
            print('not excuting sum_ function since kwargs is missing')
            return function_wrapper
        else:
            return f(*args, **kwargs)

    return function_wrapper

@print_through_functools
def sum_(*args,**kwargs):
    """Will be implemented if exclude kwarg is missing."""
    print('excuting sum_ function since kwargs is included')
    total = 0
    for number in args:
        total = number + total
        print(total)
    
    return total

class MathThing():
    def __init__(self, age=None):
        self.first = 'first_name'
        self.last = 'last_name'

        if age:
            self.age = age


sum_(10,100)
sum_(10,500, exclude=True)

print('\nchecking hashattr booleans')
name = MathThing()
name2 = MathThing(90)
# checking for age attribute in object
check = hasattr(name, 'age')
print(check)
check2 = hasattr(name2, 'age')
print(check2)