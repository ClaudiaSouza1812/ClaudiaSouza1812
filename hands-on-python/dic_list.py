# create a for loop that iterates through a list of dictionaries and prints the value of a specified key for each dictionary

# define the main function
def main():
    # define a list of dictionaries
    dic_list = [
        {"name": "Claudia", "role": "Junior Python Developer", "team": "Data Analytics"},
        {"name": "Paula", "role": "Scrum Master", "team": "Software Development"},
        {"name": "Helena", "role": "Data Strategist", "team": "Business Intelligence"},
        {"name": "Cezar", "role": "Data Scientist", "team": "Data Science"},
        {"name": "Mauricio", "role": "Data Engineer", "team": "Data Engineering"},
        {"name": "Arsalan", "role": "Python Specialist", "team": "Talent Development"},
    ]

    # call the dic_key function
    dic_key(dic_list)


# define the function to get the value of a key
def dic_key(list):

    # instruct the user
    print("You can get to know our colaborators better by the main subjects:")
    for key in list[0].keys():
        print(key)

    # get the key from the user
    args = input('\n'"Enter the information(s) that you want separated by a space:"'\n').split(" ")

    # check if the key is valid
    for word in args:
        # if the key is not valid, print a message and call the function again
        if word not in list[0].keys():
            print(f"The subject {word} is not valid, please try again"'\n')
            dic_key(list)
        # if the key is valid, continue the loop
        else:
            continue

    # print the information requested by the user
    print('\n'"Here is the information you requested for: ", end="")
    for i in range(0, len(args)):
        print(f"{args[i]} /", end=" ")
    print("\n")

    # iterate through the list of dictionaries and print the value of the key
    for dic in list:
        for i in range(0, len(args)):
            print(f"{dic[args[i]]}")
        print("-----------------")

    # print a message and end the program
    print('\n'"See you next time!")
    quit()


# call the main function
main()
