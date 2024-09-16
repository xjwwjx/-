from typing import Any


class test():
    def __init__(self):
        print("This is test class")
        self.a = 5
        self.b = 6
        print(self.func())

    def func(self) :
        print("This is func")
        self.c = self.a + self.b
        return self.a + self.b

    # def __call__(self):
    #     self.func()
    

T = test()
