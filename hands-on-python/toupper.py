# write a program that takes a list of strings as input and returns all of them in uppercase

# define the main function
def main():
    # request a list of strings from the user
    str_list = input("Enter the letter, word or sentence that you want in uppercase: "'\n').split()
    # call the to_upper function
    to_upper(str_list)


# define the function to convert the strings to uppercase
def to_upper(str_list):
    # create an empty list to store the strings in uppercase
    toupper_list = []
    # iterate through every word in the list
    for word in str_list:
        # check if any letter in the word is alphabetic
        if any(letter.isalpha() for letter in str_list[str_list.index(word)]):
            # if any letter in the word is alphabetic, convert the hole list to uppercase and store it in toupper_list
            toupper_list = [word.upper() for word in str_list]
            break
        # if no letter in the word is alphabetic, continue the loop
        else:
            continue

    # check if the list is empty
    if not toupper_list:
        # if the list is empty, print a message
        print("You need to enter at least one alphabetic word!")
        # call the main function again to start over
        main()
    # if the list is not empty, print the list
    else:
        print(f"The strings in uppercase are: {toupper_list}.".replace("['", "").replace("']", "").replace("'", "").replace(",", ""))
        exit()



# call the main function
main()
