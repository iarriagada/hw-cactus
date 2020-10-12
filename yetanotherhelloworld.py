#!/usr/bin/env python3
import random

msg_array = ['Hello, is it me you are looking for',
             'You say goodbye, I say hello. Hello, hello',
             'Hello, can you hear me',
             'Hello Darkness, my old friend',
             'Goodbye, yellow brick road',
             'Hey, I just met you, and this is crazy...',
             'Hello, I love you, won\'t you tell me your name',
             'Bye, bye, miss american pie']

print('This is the Hello world greeter')
print('How pumped do you want to feel?')

while True:
    try:
        enthus_level = input('Zen(0)/Very(1)/Normal(2)/Meh(3)'\
                             '/Areyoukiddingis2020(4)/surpriseme(5)'\
                             '/Blast-from-past(6): ')
        if int(enthus_level) is 0:
            print('***Nothing can touch me***')
        if int(enthus_level) is 0:
            print('Hello World Heck Yeah!!!')
        if int(enthus_level) is 2:
            print('Hello World!')
        if int(enthus_level) is 3:
            print('\'sup world')
        if int(enthus_level) is 4:
            print('goodbye world x(')
        if int(enthus_level) is 5:
            rand_msg = random.choice(msg_array)
            print(rand_msg)
        if int(enthus_level) is 6:
            with open('toFutureMe.txt', 'r') as f:
                print(f.readlines())
        elif int(enthus_level) not in range(0,7):
            print('There\'s nothing I can do for you, goodbye')
        break
    except ValueError:
        print('The option has to be an integer')

msg_opt = input('Do you wish to leave a message for Future You? (y/n): ')
if msg_opt in ['Y','y','yes','YES','Yes']:
    message = input('Enter message:\n> ')
    with open('toFutureMe.txt', 'w') as f:
        f.write(message)

print('Hang in there. Have a nice day')
