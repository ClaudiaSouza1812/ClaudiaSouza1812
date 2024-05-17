# Write a program that takes a string and returns the number of words in the string

# import the regular expression module to randle more than one sign as a separator
import re

# define the main function
def main():
    # declare a string variable with a sentence
    string = "Write, a program, that takes a string"
    # call the function
    num_words(string)

# define the function that takes a string and returns the number of words in the sentence
def num_words(sentence):

    # split the sentence into a list of words separated by any non-word character
    words = re.split(r'[\W\d]+', sentence)
    # remove any empty string from the list, they only appear when there are two or more non-word characters together, like "1."
    if "" in words:
        words.remove("")

    # print the number of words in the sentence
    return print(f"The number of words in the sentence is: {len(words)}")

# call the main function
main()
