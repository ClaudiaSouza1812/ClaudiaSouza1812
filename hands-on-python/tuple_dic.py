
# define the main function
def main():

    # define the tuple elements
    tup_ele = ("Claudia", 41, "Paula", 49, "Claudia", 49, True, False, "Mel")
    # call the map_frequency function
    map_frequency(tup_ele)

# define the map_frequency function
def map_frequency(tuple_list):

    # declare the freq_map variable to store the frequency of the elements
    freq_map = {}
    # iterate over the tuple_list and count the frequency of the elements
    for item in tuple_list:
        # if the element is in the freq_map, increment the frequency
        if item in freq_map:
            freq_map[item] += 1
        # if the element is not in the freq_map, add it to the freq_map
        else:
            freq_map[item] = 1

    # print the frequency map of the elements
    return print(f"The frequency map of tuples is: {freq_map}")


# call the main function
main()
