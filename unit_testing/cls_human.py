"""Demo class for testing."""
import random

import cls_human_error

AGE = random.randint(0,90)


class Human():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = AGE
         
        if first_name != 'Samus':
            raise cls_human_error.HumanError('This is not the real Samus Aran')

    def introduction(self):
        greeting = 'Hello, I am {}.  Nice to meet you'.format(
            self.first_name + ' ' + self.last_name
        )
        print(greeting)
        return greeting

