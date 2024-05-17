
# define the main function
def main():

    # request the user to input a list of numbers separated by commas or spaces, use the replace method to replace the commas with spaces and the split method to split the input by spaces and store the result in a list
    tuple_input = input("Enter a list of numbers separated by commas or spaces, press enter when done:"'\n').replace(",", " ").split()
    # call the new_even_tuple function
    new_even_tuple(tuple_input)

# define the new_even_tuple function
def new_even_tuple(tuple_list):

    # use the list comprehension to iterate over the tuple_list and check if the elements are digits and even, store the result in a new tuple
    even_tuple = tuple([num for num in tuple_list if num.isdigit() and int(num) % 2 == 0])

    # check if the even_tuple is not empty and print the new tuple with only even numbers
    if even_tuple:
        print(f"The new tuple with only even numbers is: {even_tuple}")
    # if the even_tuple is empty, print the message
    else:
        print("There are no even numbers in the tuple.")

# call the main function
main()
