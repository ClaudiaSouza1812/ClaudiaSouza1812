# Write a regular expression that matches a valid email address. For example,
# the string "example@example.com" should match

# import the necessary module to use the search method
from re import search

# define the main function
def main():

    # define the email pattern using the regular expression syntax
    email_pattern = "^[a-zA-Z0-9\.\-_]+@{1}[a-zA-Z0-9]+\.{1}[a-zA-Z]{2,3}$"
    # ask the user to enter a email address
    user_email = input("Enter a e-mail with the a format like 'example@example.com':"'\n')
    # call the check_email function
    check_email(email_pattern, user_email)


# define the check_email function
def check_email(pattern, str_email):

    # check if the email is valid using the search method, if it is valid print the result, otherwise call the main function
    if search(pattern, str_email):
        print(f"The '{str_email}' is a valid e-mail address.")
    else:
        print(f"The '{str_email}' isn't valid.")
        main()

# call the main function
main()
