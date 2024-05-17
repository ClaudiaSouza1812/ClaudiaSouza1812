# write a program to check if a word is a palindrome

# import needed modules
from time import sleep

# define the main function
def main():
    # call the function to check if the word is a palindrome
    palindrome()

# define the function to check if the word is a palindrome
def palindrome():
    # request a word from the user
    word = input("Please, enter a palindrome word:"'\n')
    # define the variable to iterate through the word
    n = len(word) - 1
    # check if the input is alphabetic
    if word.isalpha():
        # iterate through the word and check if it's a palindrome
        for i in word:
            # i is the first letter of the word, n is the last letter of the word
            if i == word[n]:
                n -= 1
                continue
            else:
                print(f"The word \"{word}\" isn't a palindrome!")
                sleep(2)
                exit()
    else:
        print("Enter an alphabetic word!")
        sleep(2)
        # call recursively the function to check if the word is a palindrome
        palindrome()
    # if the word is a palindrome, print the result
    print(f"The word \"{word}\" is a palindrome!")
    sleep(2)
    exit()

main()
