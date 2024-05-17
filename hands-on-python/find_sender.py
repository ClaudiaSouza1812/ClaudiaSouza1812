# write a program to find all the senders in a mailbox file.

total = 0
email_dict = {}
try:
    with open("mbox-short.txt", "r") as f:
        for row in f:
            if row.startswith("From:"):
                row = row.strip("From: ")
                print(f"Sender: {row}", end="")
                total += 1
                row = row.strip("Sender: ")
                if row not in email_dict:
                    email_dict[row] = 1
                else:
                    email_dict[row] += 1
except FileNotFoundError:
    print("This file does not exist.")

print(f"Total number of lines: {total}")
print(email_dict)

