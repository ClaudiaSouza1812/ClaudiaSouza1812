

# solution 1

def askFeeling():

    print('How are you feeling?')

    feeling = input()

    print('I am happy to hear that you are feeling ' + feeling + '.')

    print('Good morning!')
    askFeeling()

    print('Good afternoon!')
    askFeeling()

    print('Good evening!')
    askFeeling()

# solution 2

times_of_day = ['morning', 'afternoon', 'evening']



for time in times_of_day:

    print('Good ' + time + '!')

    print('How are you feeling?')

    feeling = input()

    print('I am happy to hear that you are feeling ' + feeling + '.')

    # solution 3

times_of_day = ['morning', 'afternoon', 'evening']

i = 0



while i < len(times_of_day):

    print('Good ' + times_of_day[i] + '!')

    print('How are you feeling?')

    feeling = input()

    print('I am happy to hear that you are feeling ' + feeling + '.')

    i += 1
