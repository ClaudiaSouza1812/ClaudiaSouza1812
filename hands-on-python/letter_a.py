# Write a program that takes a list of strings and returns a new list that contains only the
# strings that start with the letter 'a'.

# define the main function
def main():
    # create a list of strings
    strings = ["apple", "banana", "cherry", "date"]
    # call the function
    begin_with_a(strings)

# define the function that takes a list of strings and returns a new list that contains only the strings that start with the letter 'a'
def begin_with_a(words_list):

    # create a new list that contains only the strings that start with the letter 'a'
    begin_with_a = [word for word in words_list if word.startswith("a")]
    # print the new list
    return print(f"The word(s) of the list that beggin(s) with the letter 'a' is (are): {begin_with_a}.")

# call the main function
main()
