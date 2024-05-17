# You are given a list of numbers. Your task is to write Python code that calculates the average of
# these numbers using the reduce() function from the functools module and a lambda function.

import functools

def main():
    numbers = [10, 20, 30, 40, 50]
    average = functools.reduce(lambda n1, n2: n1 + n2, numbers) / len(numbers)
    print(average)
    


main()
