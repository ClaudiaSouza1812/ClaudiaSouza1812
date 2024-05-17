
from datetime import datetime

actual_time = datetime.now()
actual_time = actual_time.strftime('%H:%M:%S')

good_feelings = ['good', 'great', 'fine', 'ok', 'okay', 'not bad', 'well']
bad_feelings = ['bad', 'not good', 'not great', 'terrible', 'horrible', 'awful', 'not well']

if actual_time < '12:00:00':
    print('Good morning! How are you feeling?')
    feeling = input()
    if feeling in good_feelings:
        print('I am happy to hear that you are feeling ' + feeling + '.')
    elif feeling in bad_feelings:
        print('I am sorry to hear that you are feeling ' + feeling + '.')
    else:
        print('I hope you are feeling well.')

elif actual_time > '12:00:00' and actual_time < '18:00:00':
    print('Good afternoon! How are you feeling?')
    feeling = input()
    if feeling in good_feelings:
        print('I am happy to hear that you are feeling ' + feeling + '.')
    elif feeling in bad_feelings:
        print('I am sorry to hear that you are feeling ' + feeling + '.')
    else:
        print('I hope you are feeling well.')
else:
    print('Good evening! How are you feeling?')
    feeling = input()
    if feeling in good_feelings:
        print('I am happy to hear that you are feeling ' + feeling + '.')
    elif feeling in bad_feelings:
        print('I am sorry to hear that you are feeling ' + feeling + '.')
    else:
        print('I hope you are feeling well.')
