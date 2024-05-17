# Given a list of numbers, write a function to return a set of all prime numbers from the list.

# define the main function
def main():

    # define a list of numbers
    numbers = [1, 3, 2, 7, 9, 5, 11, 13, 15, 17, 19, 21]
    # call the prime_set function
    prime_set(numbers)


# define the function to get the prime numbers from a list
def prime_set(numbers):

    # create a set to store the prime numbers
    prime_num = set()
    # iterate through the list of numbers and check if each number is prime
    for num in numbers:
        # prime numbers are greater than 1 and have no divisors other than 1 and themselves
        if num > 1:
            # iterate through the numbers from 2 to the number and check if it has any divisors
            for div in range(2, num):
                # if the number has a divisor, break the loop
                if num % div == 0:
                    break
            # if the number has no divisors, add it to the set of prime numbers
            else:
                # add the number to the set
                prime_num.add(num)

    if len(prime_num) == 0:
        # print a message and end the program
        return print("There are no prime numbers in the list")
    
    # print the set of prime numbers
    return print(f"The prime numbers in the list are: {prime_num}")


# call the main function
main()
