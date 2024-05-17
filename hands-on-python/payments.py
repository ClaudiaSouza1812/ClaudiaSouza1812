

def computepay(hours, rate):

    try:
        hours = float(hours)
        rate = float(rate)
        if hours > 40:
            pay = hours - 40 + (rate * 1.5)
            final_pay = pay + (hours * rate)
            print("Pay:", final_pay)
        else:
            pay = hours * rate
            print("Pay:", pay)
    except ValueError:
        print("Error, please enter numeric input")
        quit()


computepay(45, 10)

