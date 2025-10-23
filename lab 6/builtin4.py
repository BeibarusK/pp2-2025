import time

def sqrt_after_miliseconds(x, y):
    time.sleep(y / 1000)

    print(f"Square root of {x} after {y} miliseconds is {x**0.5}")  

number = 25100
miliseconds = 2123

sqrt_after_miliseconds(number, miliseconds)
