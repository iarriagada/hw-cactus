#!/usr/bin/env python3
import random

randmsg = ['Hello, is it me you are looking for',
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
        enthus_level = input('Very(1)/Normal(2)/Meh(3)/Areyoukiddingis2020(4)'\
                             '/surpriseme(5): ')
        if int(enthus_level) is 1:
            print('Hello World Heck Yeah!!!')
        if int(enthus_level) is 2:
            print('Hello World!')
        if int(enthus_level) is 3:
            print('\'sup world')
        if int(enthus_level) is 4:
            print('goodbye world x(')
        if int(enthus_level) is 5:
            rand_pos = random.randint(0,7)
            print(randmsg[rand_pos])
        elif int(enthus_level) not in [1,2,3,4,5]:
            print('There\'s nothing I can do for you, goodbye')
        break
    except ValueError:
        print('The option has to be an integer')
