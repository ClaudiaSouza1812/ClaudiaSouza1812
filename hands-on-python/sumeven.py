# This program sums the even numbers in a list
# import the time module to use the sleep function
from time import sleep

# define the main function
def main():
    # call the function to sum the even numbers
    even_sum()



# define the function to sum the even numbers
def even_sum():
    # define the list to store the numbers
    list = []

    # instruct the user to enter a list of numbers
    print("Enter a list of numbers, when you're finished, enter the letter 'f'.")
    sleep(2)
    # ask the user to enter a number
    n = input("Enter a number: ")
    # define the variables to sum up the even numbers and count them
    sum = 0
    even = 0

    # while the 'f' letter isn't typed, sum the even numbers
    while n != 'f':
        # check if the input is a number
        if n.isdigit():
            # if the input is a number, convert it to int
            n = int(n)
            # add the number to the list
            list.append(n)
            # check if the number is even
            if n % 2 == 0:
                # if the number is even, sum it
                sum = sum + n
                # count the even numbers
                even = even + 1
                n = input("Enter a number: ")
            else:
                n = input("Enter a number: ")
        else:
            print(f"You need to enter a number! The numbers you already entered are: {list} and {even} of them are even numbers".replace("[", "").replace("]", ""))
            n = input("Enter a number: ")

    print(f"The sum of the even numbers are {sum}. See you next time!")
    sleep(2)
    exit()





main()
