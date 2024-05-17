

def main():
    calc_rate()

# python will optimize by storing the value 10 in memory and then pointing x and y to the same memory location
x = 10
print(id(x))
y = 10
print(id(y))

# print using the identity operator
print(x is y)

x is y # True if x and y are the same object
x is not y # True if x and y are not the same object
x == y # True if x and y have the same value


def calc_rate():

    input_hours = float(input("Please enter the hours worked: "))
    input_rate = float(input("Please enter the rate: "))
    pay = input_hours * input_rate
    print(f"Your pay is: {pay:.2f}")




main()
