# Ask user for their name:
name = input("What's your name? ")
# remove white spaces:
name = name.strip()
# capitalize user's first name:
name = name.capitalize()
# capitalize the entire user's name:
name = name.title()
# exclude spaces and capitalize all the user name at the same time:
name = name.strip().title()
# exclude spaces and capitalize all the user name at the same time as asking user its name:
name = input("What's your name? ").strip().title()

# split user's name into first and last name using the space between them:
first, last = name.split(" ")
print(f"hello, {first}")

# Say hello to user:
print("hello, ", name)

# different ways to use quote marks inside a sentence within a print statement:
print('hello "friend"')
print("hello \"friend\"")

# how to change the end of a print statement from a new line to nothing:
print("hello", end="")

# a new way to use a variable inside a print statement, using curly braces and the "f" letter
# before the sentence, which means "format" this special variable inside the curly braces:
print(f"hello, {name}")


