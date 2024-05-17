# write a program to handle the FileNotFoundError exception
from string import ascii_letters
from os import path
# define the main function
def main():
    # define the accepted characters
    acpt = ascii_letters + '.0123456789'
    # define the accepted extensions
    extlist = ['html', 'doc', 'docx', 'csv', 'txt', 'pdf']
    # define the file variable
    file = ""

    # run the loop until the file name is correct;
    while True:
        # try to get the file name from the user
        try:
            # instruct the user
            print("The valid extensions are: ", ", ".join(extlist))
            file = input("Enter a file name with a valid extension:"'\n').replace(" ", "").split(".", maxsplit=2)

            # check the file length
            if len(file) == 2:
                # if the file length is correct, check the characters and the extension
                if all(c in acpt for c in file[0]) and file[1] in extlist:
                    # if the file length is correct, the characters and the extension are correct, break the loop
                    break
                # if the file length is correct, but the characters or the extension are not, raise a ValueError exception
                else:
                    raise ValueError("Invalid file name, it must have a valid extension and a dot separating the name and the extension")
            else:
                # if the file length is not correct, raise a ValueError exception
                raise ValueError("Invalid file name, it must have a valid extension and a dot separating the name and the extension")
        # handle the ValueError exception
        except ValueError as err:
            # print the error message
            print(err)
            # ask the user to try again
            continue

    # join the file name and the extension
    file = ".".join(file)

    # call the open_file function
    open_file(file)


# define the function to open the file
def open_file(file):
    # try to open the file
    try:
        path.exists('hands-on/' + file)
        # open the file in read mode and print its content
        f = open('hands-on/' + file, "r")
        # create a variable to store the file content
        text = f.read()
        # close the file
        f.close()
        return print(text)
    # handle the FileNotFoundError exception
    except FileNotFoundError:
        print("Looks like the file you are looking for does not exist")

    # ask the user if they want to try again
    try_again = input("Do you want to try again? (y/n)"'\n').lower()
    # if the user wants to try again, call the main function again
    if try_again == "y":
        main()
    # if the user does not want to try again, print a message and end the program
    else:
        return print("End of program")




main()
