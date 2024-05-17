# Write a regular expression that matches a string that contains a number with exactly two decimal places. For example, the string "1.23"
# should match, but the string "1.234" should not match.

# import the necessary module to use the search method
from re import search

# define the main function
def main():

    # define the pattern to search for a number with exactly two decimal places
    decimal_pattern = r"^\d+\.\d{2}$"
    # ask the user to enter a number with exactly two decimal places
    user_decimal = input("Enter a number with exactly two decimal places, like '1.23':"'\n')
    # call the check_decimal function
    check_decimal(decimal_pattern, user_decimal)

# define the check_decimal function
def check_decimal(pattern, str_decimal):

    # check if the number is valid using the search method, if it is valid print the result, otherwise print the result
    if search(pattern, str_decimal):
        print(f"The number '{str_decimal}' is valid.")
    else:
        print(f"The {str_decimal} isn't valid.")

# call the main function
main()
