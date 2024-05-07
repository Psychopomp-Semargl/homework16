import math
from module1 import d
def test_function(x):
    d = pow(x,3)
    def inner_function(x):
        if d >= 0:
            print("Я в области видимости функции test_function")
    inner_function(x)
    return d
print(d)
print(test_function(5))
#print(inner_function(x))