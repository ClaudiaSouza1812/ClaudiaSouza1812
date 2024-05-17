
# write a program using try/except to take a list of numbers from the user and
# print the sum of the integers

# define the main function
def main():
    # request a list of numbers from the user
    list = input("Enter the numbers you want to sum up, separated by a space, when you're done press enter:"'\n')
    # call the function to sum up the integers
    int_sum(list)



# define the function to sum up the integers
def int_sum(list):
    # split the string into a list
    list = list.split()
    # iterate through the list and sum up the integers
    sum = 0
    for n in list:
        # use try/except to avoid errors if the user types something other than numbers
        try:
            sum += int(n)
        except ValueError:
            print("You need to type only numbers and spaces!")
            # call the main function again to start over
            main()
    # print the result
    return print(f"The sum of the integers is {sum}.", "See you next time!")




main()
