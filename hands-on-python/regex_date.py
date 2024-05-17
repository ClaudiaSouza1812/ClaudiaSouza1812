# Write a regular expression that matches a date in the format dd/mm/yyyy. For example, the string "01/01/2021" should match.

# import the regular expression (regex) module
import re

# Define the main function
def main():

    # Define the pattern to search for dates in the format dd/mm/yyyy
    # \b is a word boundary, \d is a digit, {2} is the number of digits, / is the separator, {4} is the number of digits
    date_pattern = re.compile(r"\b\d{2}/\d{2}/\d{4}\b")
    # Define the string to search for the pattern
    exe_date = input("enter a valid date with dd/mm/yyyy format:"'\n')
    # Call the check_date function
    check_date(date_pattern, exe_date)


# Define the check_date function
def check_date(pattern, date):

    # Use the search() method to find the pattern in the string
    match = pattern.search(date)
    # If the pattern is found, print the date is valid, otherwise print the date is not valid
    if match:
        print(f"The date {match.group()} is valid.")
    else:
        print(f"The date {date} is not valid.")

# Call the main function
main()

pattern = re.compile("^[a-zA-Z0-9\.\-_]+@{1}[a-zA-Z0-9]+\.{1}[a-zA-Z]{2,3}$")
print(pattern.search("smth@mail.com"))
