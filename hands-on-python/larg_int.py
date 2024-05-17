
# define a function that takes a list of integers as input and returns the largest integer in the list

# define the main function
def main():

    # request a list of integers
    integers = input("Enter a list of integers separated by a space, press enter when finishes: "'\n')
    # call the largest_int function with the list of integers as argument
    largest_int(integers)


# define the function to return the largest integer in the list
def largest_int(list):
    # split the list
    list = list.split(" ")
    # create a variable to store the largest integer
    largest = ""

    # try to convert the strings to integers
    for n in list:
        try:
            # check if the length of the string is greater than the length of the largest integer
            if len(n) >= len(str(largest)):
                # if the length of the string is greater than the length of the largest integer, convert the string to integer
                n = int(n)
                # check if the integer is greater than the largest integer
                largest = n
            # if the length of the string is not greater than the length of the largest integer, continue the loop
            else:
                continue
        # handle the ValueError exception, if the string cannot be converted to integer
        except ValueError:
            print("The strings in the list cannot be converted to integers, it will be ignored.")
            continue

    # check if the largest integer is not empty
    if largest:
        # if the largest integer is not empty, print the largest integer
        return print(f"The largest integer in the list is: {largest}")
    # if the largest integer is empty, print a message
    else:
        return print("The strings in the list cannot be converted to integers, it will be ignored.")



# call the main function
main()
