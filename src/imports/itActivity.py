from .stack import *
import string
import re

def itActivity():
    print("You sift through the assortment of computer parts and find enough parts to complete the unfinished computer.")
    print("The components you have to work with are:\n")
    print("heatsink")
    print("processor")
    print("graphics card")
    print("motherboard\n")
    print("For this computer to work you will have to install the parts in the correct order.\n")
    items=['graphicscard', 'processor', 'heatsink', 'motherboard']
    while True:
        a=Stack()
        a.push('motherboard')
        a.push('processor')
        a.push('heatsink')
        a.push('graphicscard')
        answer=a
        s=Stack()
        while True:
            if s.size() == 4:
                break
            if s.isEmpty():
                com0=input('Which item would you like to install?\n> ')
            else:
                com0=input('Which item would you like to install next?\n> ')
            com=com0.lower()
            com=re.sub('[\W\d]','',com)
            if 'help' in com:
                print("Please choose a component to insert.")
            elif com not in items:
                print("%s is not a valid computer part." %com0)
            else:
                s.push(com)
                #print s,a
        while s.top()==a.top():
            s.pop()
            a.pop()
            #print s,a
            if s.isEmpty():
                break
        if a.isEmpty():
            print("\nYou turn on the computer and it boots!! You have sucessfully built the computer.")
            print("You notice that the last person logged in was the username 'awebberl'.")
            break
        else:
            print("\nYou attempt to turn on the computer, but it will not boot. You remove all the parts. Try again.\n")

