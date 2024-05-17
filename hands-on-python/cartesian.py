# Given a list of sets, write a function to return the Cartesian product of all sets in the list,
# that is, the set of all possible tuples where the first element is from the first set, the second
# element is from the second set, and so on.

# define the main function
def main():

    # define a list of sets
    sets_list = [{1, 2, 3}, {4, 5, 6}]
    # call the cartesian_product function
    cartesian_product(sets_list)

# define the function to get the Cartesian product of a list of sets
def cartesian_product(sets_list):

    # create a set to store the Cartesian product of the sets
    cartesian = set()
    # iterate through the list of sets and get the Cartesian product of the sets
    # select an element from the first set
    for n in sets_list[0]:
        # select an element from the second set
        for i in sets_list[1]:
            # add the tuple to the set of Cartesian product
            cartesian.add((n, i))

    # print the set of Cartesian product
    return print(f"The Cartesian product of the sets are: {cartesian}")


# call the main function
main()
