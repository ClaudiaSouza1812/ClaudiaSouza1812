from time import sleep

def main():
    scores()




def scores():
    score = 0
    grade = ""
    try:
        score = float(input("Enter a score between 0.0 and 1.0: "))
    except:
        print("Error, please enter a decimal input")
        sleep(2)
        main()

    if score >= 0.9 and score <= 1.0:
        grade = "A"
        print(f"Your grade is: {grade}")
        exit()
    elif score >= 0.8 and score < 0.9:
        grade = "B"
        print(f"Your grade is: {grade}")
        exit()
    elif score >= 0.7 and score < 0.8:
        grade = "C"
        print(f"Your grade is: {grade}")
        exit()
    elif score >= 0.6 and score < 0.7:
        grade = "D"
        print(f"Your grade is: {grade}")
        exit()
    elif score < 0.6:
        grade = "F"
        print(f"Your grade is: {grade}")
        exit()
    else:
        print("Error, please enter a score between 0.0 and 1.0")
        sleep(2)
        main()




main()
