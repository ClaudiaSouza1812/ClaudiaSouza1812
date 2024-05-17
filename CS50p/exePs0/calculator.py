# ask user to insert integers numbers
x = int(input("What's x? "))
y = int(input("What's y? "))
# print the result of an arthimetic operation
print(x + y)

# ask user to insert numbers, transform them to floats and round it to the nearest integer, with 2 decimals houses after the dot
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x / y)
# print the result with a comma separation
print(f"{z:,}")

# ask user to insert numbers, transform them to floats and round it to the nearest integer, with 2 decimals houses after the dot
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x / y, 2)
# print the result with a comma separation
print(z)

# ask user to insert numbers, transform them to floats and round it to the nearest integer, with 2 decimals houses after the dot
x = float(input("What's x? "))
y = float(input("What's y? "))
z = x / y
# print the result with a comma separation
print(f"{z:.2f}")
