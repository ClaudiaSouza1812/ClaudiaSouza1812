x = 5
print(id(x))

quotient = 7 // 3
print(quotient)

# the benefit of using the floor division operator is that it always returns an integer
container_size = 100
item_size = 25
quotient = container_size // item_size
print(quotient)

# the benefit of using the modulo operator is that it always returns the remainder of a division,
# its useful to check if a number is even or odd
x = 7
remainder = x % 2
if remainder == 0:
    print(x, "is even")
else:
    print(x, "is odd")

print(remainder)

def add(x, y):
    # add the docstring to the function:
    """
    This funciton adds two numbers
    """
    return x + y

import math
print(dir(math))



