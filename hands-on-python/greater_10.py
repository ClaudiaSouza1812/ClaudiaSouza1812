
# Create a while loop that repeatedly takes user input and appends it to a list,
# but only if the input is a number greater than 10.


# define the main function
def main():

    # call the function to add integers greater than 10 to a list
    add_ints()


# define the function to add integers greater than 10 to a list
def add_ints():

    # instruct the user
    print("This program will add integer numbers greater than 10 to a list."'\n')
    print("You can add a number to the list by typing the number you want to add and press enter, type 'done' when you have finished"'\n')

    # create an empty list
    int_list = []
    # create a variable to store the user input
    int_input = ""

    # create a while loop that takes user input and adds the input to a list until the user enters "done"
    while int_input != "done" and int_input != "Done":
        # get the user input
        int_input = input("Enter an integer: ")
        # if the user input is not "done", check if the input is an integer greater than 10
        if int_input != "done" and int_input != "Done":
            # if the input is an integer greater than 10, add the input to the list
            if int_input.isdigit() and int_input > "10":
                # add the input to the list
                int_list.append(int_input)
            else:
                continue
        else:
            print(f"The integers you added are: {int_list}".replace("[", "").replace("]", ""))
            print('\n'"See you next time!")
            quit()


# call the main function
main()
