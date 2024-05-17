
# Create a while loop that generates random numbers and adds them to a list until the sum of all
# numbers in the list is greater than 100.

# import the randint function from the random module, which generates random numbers
from random import randint

# define the main function
def main():
    # call the random_numbers function
    random_numbers()

# define the function to generate random numbers
def random_numbers():
    
    # instruct the user
    print("This program will generate random numbers and add them to a list until the sum of all numbers is greater than 100."'\n')
    # create an empty list
    random_num_list = []

    # create a while loop that generates random numbers and adds them to a list until the sum of all
    while sum(random_num_list) <= 100:
        # generate a random number between 1 and 50
        random_num = randint(1, 50)
        # add the random number to the list
        random_num_list.append(random_num)

    # print the list and the sum of all numbers
    total = sum(random_num_list)
    print(f"The random numbers generated are: {random_num_list}. The sum of all numbers is {total} and it is greater than 100.")



main()
