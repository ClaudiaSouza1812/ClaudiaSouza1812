
# Create a while loop that repeatedly takes user input and keeps
# track of the highest number entered until the user enters "done".

# define the main function
def main():
    # call the function to track the highest number entered
    track_highest()


# define the function to track the highest number entered
def track_highest():

    # instruct the user
    print("This program will add integer numbers to a list and keep track of the highest number entered."'\n')
    print("You can add a number to the list by typing the number you want to add and press enter, type 'done' when you have finished"'\n')

    # create an empty list
    int_list = []
    # create a variable to store the user input
    n = ""

    # create a while loop that takes user input and adds the input to a list until the user enters "done"
    while n != "done" and n != "Done":
        # get the user input
        n = input("Enter an integer: ")
        # if the user input is not "done", check if the input is an integer
        if n != "done" and n != "Done":
            # if the input is an integer, add the input to the list
            if n.isdigit():
                int_list.append(n)
            else:
                continue
        else:
            # determine the highest number in the list
            highest = max(int_list)
            # print the list and the highest number
            print(f"The integers you added are: {int_list} and the highest number is {highest}.".replace("[", "").replace("]", ""))
            print('\n'"See you next time!")
            quit()


# call the main function
main()
