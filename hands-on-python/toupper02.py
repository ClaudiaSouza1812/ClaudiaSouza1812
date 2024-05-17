# write a program to convert the content of a text file to uppercase.

def main():

    to_upper()


def to_upper():
    with open("test.txt", "r") as f:
        text = f.read()
        print(text.upper())

main()
