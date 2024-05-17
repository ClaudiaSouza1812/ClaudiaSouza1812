# Write a program to check if a number is prime (divisible only by 1 and itself)
# import the ceil function from the math module
from math import ceil

# define the main function
def main():
    # call the function to check if the number is prime
    prime()



# define the function to check if the number is prime
def prime():

    # request a number from the user
    n = input("Enter a number:"'\n')
    # check if the input is a number

    if n.isdigit():
        # if it is, convert it to int
        n = int(n)
    # if the input isn't a number, ask the user to enter a number
    else:
        print("You need to type a number!")
        # call recursively the function to check if the number is prime
        prime()

    # check if the number is 2 (the only even prime number)
    if n == 2:
        print(f"{n} is a prime number!")
        exit()

    # check if the number is even (even numbers aren't prime)
    if n % 2 == 0:
        print(f"{n} isn't a prime number!")
        exit()

    # define the counter to check if the number is prime (set it to 1 because every number is divisible by 1)
    counter = 1
    # define the max number to iterate through (the max number is the half of the number + 1, because any number is divisible by a number higher than its half)
    max = ceil(int(n / 2) + 1)

    # iterate through the numbers
    for i in range(1, max):
        # check if the number is divisible by i
        if n % i == 0:
            # if it is, add 1 to the counter
            counter += 1
        else:
            # if it isn't, continue
            continue

    # check if the counter is 2
    if counter == 2:
        # if it is, print the result
        print(f"{n} is a prime number!")
    # if it isn't, print the result
    else:
        print(f"{n} isn't a prime number!")





# call the main function
main()
