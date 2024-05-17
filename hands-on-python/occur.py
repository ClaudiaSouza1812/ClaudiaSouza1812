# write a program to read a list of email addresses from a file and add them to a dictionary
# with the email address as the key and the number of times the email address appears in the file as the value.

email_dict = {}
try:
    with open("senders.txt", "r") as f:
        for row in f:
            row = row.strip("Sender: ")
            if row not in email_dict:
                email_dict[row] = 1
            else:
                email_dict[row] += 1
except FileNotFoundError:
    print("This file does not exist.")

print(email_dict)

