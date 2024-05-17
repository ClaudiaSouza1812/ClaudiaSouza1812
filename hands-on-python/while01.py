
# Create a while loop that repeatedly takes user input and adds the input to a list until the user enters "done".

# define the main function
def main():

    # call the add_list function
    add_list()

# define the function to add data to a list
def add_list():

    # instruct the user
    print("You can add data to a list by typing the data you want to add and press enter, type 'done' when you have finished"'\n')
    # create a variable to store the user input
    data = ""
    # create an empty list
    new_list = []

    # create a while loop that takes user input and adds the input to a list until the user enters "done"
    while data != "done" and data != "Done":
        # get the user input
        data = input("Data: ")
        # if the user input is not "done", add the input to the list
        if data != "done" and data != "Done":
            # capitalize the input
            data = data.capitalize()
            # add the input to the list
            new_list.append(data)

    # if the user input is "done", print the list and end the program
    print(f"Here are the data you added to the list: {new_list}".replace("[", "").replace("]", ""))
    print('\n'"See you next time!")
    quit()

# call the main function
main()
