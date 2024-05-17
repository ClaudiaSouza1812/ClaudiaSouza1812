# Write a regular expression that matches a string that starts with a word, followed by one or more whitespace characters, followed by another word.
# For example, the string "hello world" should match


# import the necessary module to use the search method
from re import search

# define the main function
def main():

    # define the pattern to search for words and whitespace
    words_pattern = r"^\w[A-Za-z]+\s+\w[A-Za-z]+$"
    # ask the user to enter a sentence with the format 'word word'
    user_words = input("Enter a sentence with the format 'word word', which is a word followed by a whitespace and another word:"'\n')
    # call the check_words function
    check_words(words_pattern, user_words)


# define the check_words function
def check_words(pattern, str_words):

    # check if the sentence is valid, if it is print the result, otherwise print the result
    if search(pattern, str_words):
        print(f"The sentence '{str_words}' is valid.")
    else:
        print(f"The sentence '{str_words}' is invalid.")

# call the main function
main()
