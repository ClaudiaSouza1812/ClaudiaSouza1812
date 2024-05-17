# Write a regular expression that matches a phone number in the format xxx-xxx-xxxx, where x is a digit.
# For example, the string "123-456-7890" should match

# import the necessary module
from re import search

# define the main function
def main():

    # define the phone pattern
    phone_pattern = r'\d{3}-\d{3}-\d{4}'
    # ask the user to enter a phone number
    phone_number = input("Enter a phone number in the format xxx-xxx-xxxx, where x is a digit:"'\n')
    # call the check_phone function
    check_phone(phone_pattern, phone_number)

# define the check_phone function
def check_phone(pattern, str_phone):

    # check if the phone number is valid or not using the search method
    if search(pattern, str_phone):
        # print the result if the phone number is valid
        print(f"The phone number '{str_phone}' is valid.")
    else:
        # print the result if the phone number is invalid and call the main function
        print(f"The data entered '{str_phone}' is invalid.")
        main()

# call the main function
main()
