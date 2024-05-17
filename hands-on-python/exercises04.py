# Given a text document, write a Python script that extracts all the phone numbers from the text using regular expressions.
# Phone numbers can be in different formats (e.g., (123) 456-7890 or 123-456-7890)

import re

def main():

    phone_pattern = re.compile(r"\b\d{3}-\d{3}-\d{4}\b")
    text_exe = "123-456-7890"

    check_phone(phone_pattern, text_exe)

def check_phone(pattern, file):
    match = pattern.findall(file)
    if match:
        print(f"The phone number {match} is valid.")
    else:
        print(f"The phone number {file} is not valid.")

main()

# list comprehension
list = [x for x in range(10) if x % 2 == 0]
print(list)

# is equivalent to
for x in range(10):
    if x % 2 == 0:
        print(x, end=", ")

# nested list comprehension, the output will be a list of tuples
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(combs)

# is equivalent to
combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combs)

lis = [num for num in range(100)
       if num % 2 == 0 if num % 5 == 0]
print(lis)

lis = ["Even" if num % 2 == 0 else "odd" for num in range(10)]
print(lis)

# lambda functions
# lambda functions are small anonymous functions that can have any number of arguments, but can only have one expression.
# sintax: lambda parameters: expression

fct = lambda x, y: x + y
print(fct(5, 6))

def myfunc(n):
    def doubler(x):
        return n * x
    return doubler

mydoubler = myfunc(2)

result = mydoubler(11)

print(id(myfunc))
print(id(mydoubler))
print(id(result))

# is equivalent to
def myfunc(n):
    return lambda a : a * n

print(myfunc(2)(11))

str1 = "welcome"

rev_upper = lambda x: x[::-1].upper()

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)

ages = [13, 90, 17, 59, 21, 60, 5]

adults = list(filter(lambda age: age > 18, ages))
print(adults)

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x * 2, li))
print(final_list)

animals = ['dog', 'cat', 'parrot', 'rabbit']
uppered_animals = list(map(lambda animal: str.upper(animal), animals))

from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
summ = reduce(lambda a, b: a + b, nums)
print(summ)

# a frozenset is a set that is immutable, or unchangeable after its creation (i.e., elements can't be added or removed).
frz1 = frozenset([1, 2, 3, 4, 5])


















