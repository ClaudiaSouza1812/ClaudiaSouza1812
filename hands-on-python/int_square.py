# write a for loop that prints the square (the number * itself) of each integer in a list of integers

# import the pow function from the math module, which returns the value of the first argument raised to the power of the second argument
from math import pow

# define the main function
def main():

    # prompt the user to enter a list of integers
    int_list = input("Enter a list of integers separated by spaces: ").split(" ")
    # remove any non-integer characters from the list
    int_list = list(filter(str.isdigit, int_list))
    # convert the list of integers from strings to integers
    int_list = list(map(int, int_list))
    # check if the list of integers is empty
    if len(int_list) == 0:
        print("You didn't enter any integers separated by spaces.")
        main()

    # call the int_square function and pass the list of integers as an argument
    int_square(int_list)

# define the int_square function
def int_square(list):
    # iterate through the list of integers and print the square of each integer
    for n in list:
        print(f"The square of {n} is: ", int(pow(n, 2)))

# call the main function
main()
