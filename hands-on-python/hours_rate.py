
hours = float(input("Enter your hours:" ))
rate = float(input("Enter your rate:" ))
if hours > 40:
    overtime = hours - 40
    pay = 40 * rate + overtime * rate * 1.5
else:
    pay = hours * rate

print("Pay:", pay)
