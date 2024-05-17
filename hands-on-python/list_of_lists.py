
# Create a for loop that iterates through a list of lists and prints the sum of the elements in each sub-list

# define the main function
def main():

    # define the list of lists
    list_of_lists = [[5, 9, 7], [2, 3, 4], [8, 7, 6], [0, 1, 2]]
    # call the function to sum the numbers in the sub-lists
    sum_of_lists(list_of_lists)

# define the function to sum the numbers in the sub-lists
def sum_of_lists(array_of_lists):
    # iterate through each sub-list array of lists
    for sub_list in array_of_lists:
        # define the sum variable
        sum = 0
        # iterate through each number in the sub-list
        for n in sub_list:
            # add the number to the sum
            sum += n
        # print the sum of the numbers in the sub-list
        print(f"The sum of the numbers in the sub-list {sub_list} is {sum}.")
    # print a message to say goodbye
    print("See you next time!")
    # exit the program
    exit()

# call the main function
main()
