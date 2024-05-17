# Find the sum of all the multiples of 3 or 5 below 1000

# Author: Claudia Simone de Souza
# Date: 2021-04-25
# Python version: 3.8.2
# License: MIT
# GitHub: ClaudiaSouza1812

# define the main function
def main():

    # call the function
    sum_mult()


# define the function
def sum_mult():

    # declare a variable to store the sum of all the multiples of 3 or 5 below 1000
    sum = 0
    # loop through the range of 1000
    for i in range(1000):
        # check if the number is a multiple of 3 or 5
        if i % 3 == 0 or i % 5 == 0:
            # if it is, add it to the sum
            sum += i
        # if it is not, continue the loop
        else:
            continue

    # print the sum of all the multiples of 3 or 5 below 1000
    print(f"The sum of all the multiples of 3 or 5 below 1000 is: {sum}.")



# call the main function
main()
