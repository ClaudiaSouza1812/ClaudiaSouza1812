# import the numpy library to use the unique function
import numpy as np

# define the main function
def main():
    # define the tuple elements
    tup_ele = ("Claudia", 41, "Paula", 49, "Claudia", 49, True, False, "Mel")
    # call the unique_ele function
    unique_ele(tup_ele)

# define the unique_ele function
def unique_ele(tuple_list):

    # convert the tuple_list to a list and use the numpy unique function to find the unique elements
    tuple_list = list(tuple_list)
    unique_list = np.unique(tuple_list)

    # print the unique elements
    return print(f"The unique elements are: {tuple(unique_list)}")


# call the main function
main()
