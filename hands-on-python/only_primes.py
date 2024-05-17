# Write a program that takes a list of integers and returns a
# new list that contains only the prime numbers from the original list.

# define the main function
def main():

    # create a list of integers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    # call the function
    only_primes(numbers)

# define the function that takes a list of integers and returns a new list that contains only the prime numbers
def only_primes(numbers_list):

    # create a new list that contains only the prime numbers
    prime_numbers = []
    # iterate through the numbers in the list
    for number in numbers_list:
        # if the number is greater or equal 2, check if it's a prime number
        if number >= 2:
            # use the loop for else statement to check if the number is a prime number,
            # the else statement will only run if the loop completes without a break
            # the break is only executed if the number is not a prime number,
            # wich means it's divisible by any number in the range besides 1 and itself
            for i in range(2, number):
                # if the number is divisible by any number in the range, it's not a prime number
                if (number % i) == 0:
                    break
            # if the number is not divisible by any number in the range, it's a prime number
            else:
                prime_numbers.append(number)

    # print the new list that contains only the prime numbers
    return print(prime_numbers)

# call the main function
main()
