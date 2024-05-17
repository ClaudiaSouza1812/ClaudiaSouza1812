
# write a program to print the largest number of a list

# import the time module to use the sleep function
from time import sleep

# define the main function
def main():
    # call the function to check the largest number
    largestnumber()


# define the function to check the largest number
def largestnumber():

    # ask the user to enter the numbers
    num_list = input("Enter a list of positive numbers separated by a space:"'\n').split()
    # define the list to store the numbers
    largest = "0"
    # keep asking for numbers until the 'f' letter is typed
    for i in range(len(num_list)):
        # if the number is a digit
        if num_list[i].isdigit():
            # if it is, check if it's larger than the previous number
            if len(num_list[i]) >= len(largest):
                # if it is, replace the previous number
                largest = num_list[i]
            else:
                continue
        else:
            continue

    # print the largest number
    if largest == "0":
        print("You need to type at least one number!")
        sleep(2)
        main()
    else:
        print(f"The largest number is {largest},".replace("[", "").replace("]", ""), "see you next time!")
        sleep(2)
        exit()

# call the main function
main()




