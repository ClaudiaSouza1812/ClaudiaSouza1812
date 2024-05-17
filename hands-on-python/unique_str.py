
# Create a while loop that repeatedly takes user input and appends
# it to a list, but only if the input is a unique string.


# define the main function
def main():

    # call the function to add unique strings to a list
    add_unique_str()


# define the function to add unique strings to a list
def add_unique_str():

    # instruct the user
    print("This program will add unique words to a list. If you enter a word that is already in the list, it will not be added."'\n')
    print("You can add a word to the list by typing the word you want to add and press enter, type 'done' when you have finished"'\n')

    # create an empty list
    str_list = []
    # create a variable to store the user input
    str_input = ""

    # create a while loop that takes user input and adds the input to a list until the user enters "done"
    while str_input != "done" and str_input != "Done":
        # get the user input
        str_input = input("Enter a word: ").capitalize()
        # if the user input is not "done", check if the input is a unique string
        if str_input != "done" and str_input != "Done":
            # if the input is a unique string and is alphabetical, add the input to the list
            if str_input.isalpha() and str_input not in str_list:
                # capitalize the input
                str_input = str_input.capitalize()
                # add the input to the list
                str_list.append(str_input)
            else:
                print(f"You entered '{str_input}'. Remember to enter only one word a time and make sure it is unique."'\n')
                continue
        else:
            print(f"The unique words you added are: {str_list}".replace("[", "").replace("]", ""))
            print('\n'"See you next time!")
            quit()



main()
