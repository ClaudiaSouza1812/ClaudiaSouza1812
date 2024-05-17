# Write a program that takes a string and returns the number of vowels in the string.

# define the main function
def main():
    # declare a string variable with a sentence
    string = "Hello, world!"
    # call the function
    num_vowels(string)

# define the function that takes a string and returns the number of vowels in the string
def num_vowels(characters):

    # define the vowels
    def_vowels = "aeiou"
    # create a variable to store the total number of vowels
    total = 0
    # iterate through the characters in the string
    for letter in characters:
        # if the letter is a vowel, add 1 to the total
        if letter in def_vowels:
            total += 1
    # print the total number of vowels
    return print(f"The total number of vowels in the sentence is: {total}")

# call the main function
main()
