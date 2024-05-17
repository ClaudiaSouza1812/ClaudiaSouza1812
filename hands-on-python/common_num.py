# Write a program that takes two lists of numbers and returns a new list
# that contains only the numbers that are common to both lists.

# define the main function
def main():
    # create two lists of numbers
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = [2, 4, 6, 8, 10, 12, 14, 16, 18]
    # call the function
    common_num(list1, list2)

# define the function to compare the numbers in the two lists
def common_num(list_num_1, list_num_2):
    # create a new list that contains only the numbers that are common to both lists
    common_num = [n for n in list_num_1 if n in list_num_2]
    # if the new list is not empty, print the common number(s)
    if len(common_num) > 0:
        return print(f"The common number(s) present in both lists is (are): {common_num}.")
    # if the new list is empty, print the message
    else:
        return print("There are no common numbers present in both lists.")

# call the main function
main()
