# Given two sets A and B, write a function to return the symmetric difference between them as a new set.
# The symmetric difference is the set of elements that are in either A or B, but not in both.

# define the main function
def main():

    # define two sets, that are collections of unique elements that are unordered, undindexed and unchangeable
    set1 = {"Claudia", "Paula", "Helena", "Cezar", "Mauricio", "Arsalan"}
    set2 = {"Kelly", "Cida", "Claudia", "Paula", "Jonatan", "Mel"}

    # call the sym_diff function
    sym_diff(set1, set2)


# define the function to get the symmetric difference between two sets
def sym_diff(set1, set2):

    # get the symmetric difference between the sets using the symmetric_difference() method,
    # that returns a new set with the elements that are in either set1 or set2, but not in both.
    # It can also be done using the ^ operator, like this: set3 = set1 ^ set2
    set3 = set1.symmetric_difference(set2)

    # check if there are no elements in the symmetric difference between the sets
    if len(set3) == 0:
        # print a message and end the program
        return print("There are no elements in the symmetric difference between the sets")

    # print the symmetric difference between the sets
    return print(f"The symmetric difference between the sets is: {set3}")

# call the main function
main()
