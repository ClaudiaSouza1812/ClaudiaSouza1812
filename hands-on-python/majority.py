# write a program to check the majority of the voters

# define the main function
def main():
    # call the function to check the majority
    majority()




# define the function to check the majority
def majority():
    # request the age from the user
    age = input("Enter your age:"'\n')
    # check if the input is a number
    if age.isdigit():
        # if the input is a number, convert it to int
        age = int(age)
        # check if the user is old enough to vote
        if age >= 18:
            print("You're old enough to vote!")
            exit()
        else:
            print("You aren't old enough to vote!")
            exit()
    # if the input isn't a number, ask the user to enter a number
    else:
        print("You need to enter a number!")
        majority()


main()
