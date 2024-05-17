
def main():
    x = int(input("What's x? "))
    print("x squared is", square2(x))



def square1(n):
    return n * n


def square2(n):
    return n ** 2


def square3(n):
    return pow(n, 2)


main()
