# Write a program that takes a list of numbers and returns the largest number in the list.

# define the main function
def main():

    # your code here
    # create a list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # call the function
    largest_number(numbers)

# define the function that takes a list of numbers and returns the largest number in the list
def largest_number(numbers_list):

    # instruct users about the program
    print('\n'"This program takes a list of numbers and returns how many digits the largest number has.")
    # convert the list to a string and remove the commas and brackets
    numbers_list = str(numbers_list).replace(",", "").replace("[", "").replace("]", "").split()
    # determine the length of the numbers in the list using the set() function, which returns the unique lengths of the numbers
    lengths = len(set([len(x) for x in numbers_list]))
    # if the length of all the numbers in the list is the same, print the message with the length and the numbers
    if lengths == 1:
        return print('\n'f"All numbers have the same length, {lengths}, the numbers are {numbers_list}.")
    # if the length of the numbers in the list is not the same, print the message with the length and the largest number
    else:
        largest = max(numbers_list, key=len)
        return print('\n'f"The largest number has {lengths} digits and is: {largest}")


# call the main function
main()
