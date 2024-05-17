# write a program to return a list of strings that can be converted to floats

# define the main function
def main():
    # define the list of numbers
    numbers = input("Enter a list of numbers separated by a space, press enter when finishes: ")
    # call the to_float function
    to_float(numbers)


# define the function to convert the strings to floats
def to_float(list):

    # split the list
    list = list.split(" ")
    # create an empty list to store the floats
    float_list = []

    # try to convert the strings to floats
    for i in range(len(list)):
        try:
            # append the floats to the list
            float_list.append(float(list[i]))
        # handle the ValueError exception, if the string cannot be converted to float
        except ValueError:
            # continue the loop
            continue

    # check if the list is empty
    if len(float_list) == 0:
        # if the list is empty, print a message
        return print("The strings in the list cannot be converted to floats.")
    # if the list is not empty, print the list
    else:
        return print(f"The strings succesfully converted to floats are: {float_list}.")



# call the main function
main()
