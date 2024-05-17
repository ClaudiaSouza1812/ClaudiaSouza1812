# Write a function to find the most common elements in a tuple
# import needed functions
from collections import Counter

# define the main function
def main():

    # define the tuple elements
    tup_ele = ("Claudia", 41, "Paula", 49, "Claudia", 49, True, False, "Mel")
    # call the find_common function
    find_common(tup_ele)

# define the find_common function
def find_common(tuple_list):

    # use the Counter function to count the elements in the tuple and the most_common function to find the most common elements
    common_list = Counter(tuple_list).most_common()
    # declare the variable freq to store the frequency of the most common elements
    freq = common_list[0][1]
    # print the fisrt part of the output
    print(f"The most common itens, apearing {freq} times, are: ")
    # iterate over the common_list and print the most common elements
    for i in common_list:
        # if the frequency of the element is equal to the freq variable, print the element
        if i[1] == freq:
            print(i[0])
        # if the frequency of the element is different from the freq variable, break the loop
        else:
            break
# call the main function
main()
