
# write a program to check the largest number divisible by 3

# import the time module to use the sleep function
from time import sleep

# define the main function
def main():
    # call the function to check the largest number divisible by 3
    largestnumber()



# define the function to check the largest number divisible by 3
def largestnumber():

    # instruct the user to enter a list of numbers
    print("Enter a list of numbers, when you're finished, enter the letter 'f'.")
    sleep(2)
    # ask the user to enter a number
    n = input("Enter a number:"'\n')
    # define the list to store the numbers
    list = [0]
    # keep asking for numbers until the 'f' letter is typed
    while n != 'f':
        # if the number is a digit
        if n.isdigit():
            # if it is, convert it to int
            n = int(n)
            # check if the number is divisible by 3
            if n % 3 == 0:
                # if it is, check if it's larger than the previous number
                if n > list[0]:
                    # if it is, replace the previous number
                    list[0] = n
                    n = input("Enter a number:"'\n')
                else:
                    n = input("Enter a number:"'\n')
            else:
                n = input("Enter a number:"'\n')
        # if the number isn't a digit, ask the user to enter a number
        else:
            print("You need to type a number!")
            n = input("Enter a number:"'\n')

    # print the largest number divisible by 3
    print(f"The largest number divisible by 3 is {list[0]}".replace("[", "").replace("]", ""), "see you next time!")
    sleep(2)
    exit()




main()
