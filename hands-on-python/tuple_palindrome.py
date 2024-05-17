# Write a function to check if a given tuple is a palindrome, meaning the elements are the same in reverse order

# define the main function
def main():

    # define the tuple elements
    str_tuple = ("civic", "level", "radar", "rotor", "kayak", "claudia")
    # call the check_pallindrome function
    check_pallindrome(str_tuple)

# define the check_pallindrome function
def check_pallindrome(tuple_list):

    # declare the pall_list variable to store the pallindrome words
    pall_list = []
    # iterate over the tuple_list and check if the elements are pallindromes
    for word in tuple_list:
        # check if the word is a pallindrome by comparing it with its reverse
        if word == word[::-1]:
            # if the word is a pallindrome, append it to the pall_list
            pall_list.append(word)
        # if the word is not a pallindrome, continue the loop
        else:
            continue

    # check if the pall_list is not empty and print the pallindrome words
    if len(pall_list) > 0:
        print(f"The pallindrome words in the tuple are: {pall_list}")
    # if the pall_list is empty, print the message
    else:
        print("There are no pallindrome words in the tuple.")


# call the main function
main()
