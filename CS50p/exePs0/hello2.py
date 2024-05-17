
def main():
    # ask user for their name:
    name = input("What's your name? ")
    hello(name)
    hello()




# define a function that has one parameter, arg, and returns a string using the print function:
def hello(arg):
    print("hello,", arg)


# define a function that has one parameter with a pre defined value, arg, if the function
# is called with an argument, the pre defined value will be replaced by the argument,
# and returns a string using the print function:
def hello(arg="world"):
    print("hello,", arg)




main()
