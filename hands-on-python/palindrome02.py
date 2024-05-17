# Write a program that takes a list of strings and returns a new list that contains only the strings that are palindrome.

# define the main function
def main():

    # create a list of strings
    strings = ["madam", "level", "civic"]
    # call the function
    is_palindrome(strings)

# define the function that takes a list of strings and returns a new list that contains only the palindromes
def is_palindrome(words_list):

    # create a new list that contains only the strings that are palindrome, that is, the word is the same when read forward and backward
    palindromes_list = [word for word in words_list if word == word[::-1]]
    # if the new list is not empty, print the palindrome(s)
    if len(palindromes_list) > 0:
        return print(f"The word(s) of the list that is (are) palindrome(s) is (are): {palindromes_list}.")
    # if the new list is empty, print the message
    else:
        return print("There are no palindromes in the list.")

# call the main function
main()
