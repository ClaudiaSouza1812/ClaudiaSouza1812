# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

# Author: Claudia Simone de Souza
# Date: 2021-04-25
# Python version: 3.8.2
# License: MIT
# GitHub: ClaudiaSouza1812

# define the main function
def main():

    # declare a variable to store the maximum value
    max_val = 4000000
    # call the function
    sum_even_fibo(max_val)


# define the function
def sum_even_fibo(max_range):

    # declare a variable to store the sum of the even-valued terms in the Fibonacci sequence
    sum = 0
    # declare a list to store the Fibonacci sequence with the first two terms
    fibo = [1, 2]
    # declare a variable to store the index of the list
    i = 2
    # loop through the Fibonacci sequence until the sum is less than the maximum value, which is 4 million
    while sum <= max_range:
        # add the next term to the list
        fibo.append(fibo[i - 2] + fibo[i - 1])
        # check if the term is even
        if fibo[i] % 2 == 0:
            # if it is, add it to the sum
            sum += fibo[i]
        # if it is not, continue the loop
        i += 1

    # print the sum of the even-valued terms in the Fibonacci sequence
    print(f"The sum of the even-valued terms in the Fibonacci sequence whose values do not exceed {max_range} is: {sum}.")

# call the main function
main()
