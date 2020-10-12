#!/usr/bin/env python3

print('This is the Hello world greeter')
print('How pumped do you want to feel?')
while True:
    try:
        enthus_level = input('Zen(0)/Very(1)/Normal(2)/Meh(3)/Areyoukiddingis2020(4): ')
        if int(enthus_level) is 0:
            print('***Nothing can touch me***')
        if int(enthus_level) is 1:
            print('Hello World Yeah!!!')
        if int(enthus_level) is 2:
            print('Hello World!')
        if int(enthus_level) is 3:
            print('\'sup world')
        if int(enthus_level) is 4:
            print('goodbye world x(')
        elif int(enthus_level) not in range(0,5):
            print('There\'s nothing I can do for you, goodbye')
        break
    except ValueError:
        print('The option has to be an integer')
