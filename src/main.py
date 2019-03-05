from imports.alphaCipher import *
from imports.itActivity import *
from imports.map import *
from imports.stack import *

def helpMe():
    print("Why don't you try to LOOK AROUND, EXAMINE/READ/PICK UP an object, or LEAVE ROOM. You can")
    print("also look at your MAP if you feel lost.")

def bag():
    print("You take your bag off and take a look at what you have: ")
    if len(inv) == 0:
        print("You currently have nothing in your bag besides that MAP you always have with you...")
    for item in inv:
        print("-%s" %(item))

def hallway():
    while True:
        if "Kool-Aid" in inv:
            kool=True
        else:
            kool=False
        com=input('>').lower()
        if len(com.strip()) <= 0:
            continue
        elif "help" in com:
            print("""Please ENTER a room:

Jim's Office
Ron's Office
Kevin's Office
Ru's Office
East Hallway
West Hallway
Outside Cs Lab""")
        elif "look" in com and "around" in com:
            print("You look around to see the West and East wings of the hall and Kevin's, Jim's, Ron's, and Ru's offices in front of you.")
            print("The area in front of the cs lab is behind you now.")
        elif "inv" in com or "bag" in com:
            bag()
        elif "drink" in com:
            if kool:
                print("You take a Kool-Aid out of the cooler and you take a drink and you begin")
                print("to feel fuzzy. The office begins to fade away eventually leading to complete darkness.....")
                print()
                print()
                print()
                print("..............")
                print("..............")
                print("..............\n")
                print("You begin to wake up and you realise that you are back where you started, in the CS Lab...")
                print("Bag empty...You have no idea what just happened...\n")
                del inv[:]
                del dummy[:]
                csLab()
            else:
                print("You never took a Kool-Aid from Jim's Office...")
        elif "cs" in com or "lab" in com:
            print("You go back out of the hallway and walk in front of the CS Lab. You are now facing the door")
            print("to the CS Lab. The men's and women's bathrooms are next to you and the IT Lab is to your right.")
            stack.push('hallway()')
            outsideCsLab()
        elif "outside" in com and not "cs" in com:
            print("If you want to go outside you have to go down the east hallway...")
        elif "map" in com:
            print("You take out a map from your bag and look at it:\n")
            reschMapHall()
        elif "east" in com:
            print("You are now in the east wing of the hall. You can see two rooms. The room closest to you is room 103")
            print("while the room further down is room 105. The center of the hall is behind you.")
            stack.push('hallway()')
            eastHallway()
        elif "west" in com:
            print("You arrive at the west wing of the hallway. It is almost pitch black here. You cannot")
            print("see a thing...")
            westHallway()
        elif "hallway" in com or "hall" in com or "center" in com:
            print("You are already in the hallway...")
        elif "jim" in com:
            jimOffice()
        elif "ron" in com:
            ronOffice()
        elif "kevin" in com:
            kevinOffice()
        elif "ru" in com:
            ruOffice()
        elif "inv" in com:
            print(inv)
        elif "leave" in com or "exit" in com or "out" in com:
            print("Please specify which room you want to go to or use the BACK command to go to a room you were in previously.")
        elif "back" in com:
            if stack.top() == "outsideCsLab()":
                print("You go back out of the hallway and walk in front of the CS Lab. You are now facing the door")
                print("to the CS Lab. The men's and women's bathrooms are to your left and the IT Lab to our right.")
                stack.push('hallway()')
                outsideCsLab()
            if stack.top() == "westHallway()":
                print("You are back in the West Hallway.")
                stack.pop()
            if stack.top() == "eastHallway()":
                print("You are back in the East Hallway.")
                stack.pop()
            else:
                stack.pop()
        else:
            print("I do not understand your command.")

def westHallway():
    while True:
        if "Kool-Aid" in inv:
            kool=True
        else:
            kool=False
        if "guineamoved" in dummy:
            moved=True
        else:
            moved=False
        if "Guinea Pig" in inv:
            pig=True
        else:
            pig=False
        if "Flashlight" in inv:
            light=True
        else:
            light=False
        com=input('>').lower()
        if len(com.strip()) <= 0:
            continue
        elif "flash" in com or "light" in com:
            if light and not pig and not moved:
                print("You take the flashlight out of your bag and turn it on. Suddenly you hear a scurrying sound. The creature who made")
                print("the sound appears to have moved to the east hallway...")
                dummy.append('guineamoved')
            elif light and moved:
                print("You take the flashlight out of your bag and turn it on. Nothing much to see...")
            else:
                print("You don't have a flashlight with you... You remember seeing one in the IT Lab.")
        elif "inv" in com or "bag" in com:
            bag()
        elif "map" in com:
            print("You take a map out of your bag and look at it:\n")
            reschMapWest()
        elif "west" in com:
            print("You are already in the West Hallway.")
        elif "look" in com and "around" in com:
            print("You take a look around and see nothing but darkness. You can see the light coming from the center of the hallway.")
        elif "leave" in com or "exit" in com or "back" in com or "center" in com or "hall" in com:
            print("You turn around and walk back to the center of the hallway")
            stack.push('westHallway()')
            hallway()
        elif "help" in com:
            helpMe()
        elif "drink" in com:
            if kool:
                print("You take a Kool-Aid out of the cooler and you take a drink and you begin")
                print("to feel fuzzy. The office begins to fade away eventually leading to complete darkness.....")
                print()
                print()
                print()
                print("..............")
                print("..............")
                print("..............\n")
                print("You begin to wake up and you realise that you are back where you started, in the CS Lab...")
                print("Bag empty...You have no idea what just happened...\n")
                del inv[:]
                del dummy[:]
                csLab()
            else:
                print("You never took a Kool-Aid from Jim's Office...")
        else:
            print("I don't understand your command.")

def eastHallway():
    while True:
        if "Kool-Aid" in inv:
            kool=True
        else:
            kool=False
        com=input('>').lower()
        if len(com.strip()) <= 0:
            continue
        elif "map" in com:
            print("You take a map out of your bag and look at it:\n")
            reschMapEast()
        elif "inv" in com or "bag" in com:
            bag()
        elif "drink" in com:
            if kool:
                print("You take a Kool-Aid out of the cooler and you take a drink and you begin")
                print("to feel fuzzy. The office begins to fade away eventually leading to complete darkness.....")
                print()
                print()
                print()
                print("..............")
                print("..............")
                print("..............\n")
                print("You begin to wake up and you realise that you are back where you started, in the CS Lab...")
                print("Bag empty...You have no idea what just happened...\n")
                del inv[:]
                del dummy[:]
                csLab()
            else:
                print("You never took a Kool-Aid from Jim's Office...")
        elif "outside" in com:
            print("You attempt to walk out the door, but a wild Snorlax appears to be blocking the way.")
        elif "east" in com:
            print("You are already in the East Hallway.")
        elif "help" in com:
            print("""Please ENTER a room:

Room 103
Room 105
Hallway (Center)""")
        elif "look" in com and "around" in com:
            print("You see two rooms, Room 103 and 105. The center of the hallway is behind you.")
        elif "leave" in com or "exit" in com or "out" in com:
            print("Please specify which room you want to go to or use the BACK command to go to a room you were in previously.")
        elif "hall" in com or "center" in com or "behind" in com:
            print("You turn around and walk back to the center of the hallway")
            stack.push('eastHallway()')
            hallway()
        elif "back" in com:
            if stack.top()=='hallway()':
                print("You turn around and walk back to the center of the hallway")
                stack.push('eastHallway()')
                hallway()
            else:
                stack.pop()
        elif "103" in com:
            room103()
        elif "105" in com:
            room105()
        else:
            print("I don't know what you want me to do...")

def outsideCsLab():
    while True:
        if "Kool-Aid" in inv:
            kool=True
        else:
            kool=False
        com = input('>').lower().strip()
        if len(com.strip()) <= 0:
            continue
        elif "help" in com:
            print("""Please ENTER a room:

CS Lab
IT Lab
Women's Bathroom
Men's Bathroom
Hallway""")
        elif "look" in com and "around" in com:
            print("You take a look around and see mutiple rooms. You can see the CS Lab, IT Lab, the Mens and Womens Bathroom, and the hallway...")
        elif "inv" in com or "bag" in com:
            bag()
        elif "outside" in com and "cs" in com:
            print("You are already outside of the CS Lab.")
        elif "drink" in com:
            if kool:
                print("You take a Kool-Aid out of the cooler and you take a drink and you begin")
                print("to feel fuzzy. The office begins to fade away eventually leading to complete darkness.....")
                print()
                print()
                print()
                print("..............")
                print("..............")
                print("..............\n")
                print("You begin to wake up and you realise that you are back where you started, in the CS Lab...")
                print("Bag empty...You have no idea what just happened...\n")
                del inv[:]
                del dummy[:]
                csLab()
            else:
                print("You never took a Kool-Aid from Jim's Office...")
        elif "map" in com:
            print("You take a map out of your bag and look at it:\n")
            reschMapOutside()
        elif "cs" in com:
            print("You are now in the CS Lab.")
            csLab()
        elif "it" in com or "north east" in com or "northeast" in com or "right" in com:
            print("You are now in the IT Lab. There are computers strewn everywhere.")
            print("There are a couple of tables in the middle of the room.")
            itLab()
        elif "women" in com or "woman" in com:
            womenBathroom()
        elif "men" in com or "man" in com:
            menBathroom()
        elif "bathroom" in com or "straight" in com:
            while True:
                a = input("Which bathroom do you want to go to?: ").lower().strip("'")
                if "women" in a or "woman" in a or "lady" in a or "girl" in a or "female" in a:
                    womenBathroom()
                if "men" in a or "man" in a or "guy" in a or "male" in a:
                    menBathroom()
                else:
                    print("I don't understand you... What were you saying again?")
        elif "hall" in com or "center" in com:
            print("You are now in the hallway. It runs from east to west. There are offices along the hallway")
            print("that are directly in front of you. The few that you recognize are Kevin's, Jim's, Ron's, and Ru's.")
            stack.push('outsideCsLab()')
            hallway()
        elif "leave" in com or "exit" in com or "out" in com:
            print("Please specify which room you want to go to or use the BACK command to go to a room you were in previously.")
        elif "back" in com:
            if stack.top()=='csLab()':
                print("You have stepped back into the CS Lab.")
                stack.pop()
            elif stack.top()=='itLab()':
                print("You have stepped back into the IT Lab.")
                stack.pop()
            elif stack.top()=='hallway()':
                print("You have stepped back into the Hallway (Center).")
                stack.pop()
            else:
                stack.pop()
        else:
            print("I don't know what you are trying to do...")


def start():
    print("""
The day is May 8, 2012. You are going to the Resch center to finish
the Data Structures Project before the due date the next morning.
When you arrive at the computer science lab, you notice that the
door to the CSIT Guinea pig cage is open. You take a look inside
and the guinea pig is no longer there. Something seems to be
wrong with the cage door. You are standing there perplexed�
""")
    while True:
        com=input('>').lower()
        if "Jim's Key" in inv:
            key=True
        else:
            key=False

        if len(com.strip()) <= 0:
            continue
        elif "help" in com:
            helpMe()
        elif "map" in com:
            print("You take out a map from your bag and look at it:\n")
            reschMapCS()
        elif "inv" in com or "bag" in com:
            bag()
        elif "pig" in com and "back" in com or "pig" in com and "put" in com:
            print("You have to find the pig before you do that...")
        elif "leave" in com or "exit" in com or "back" in com or "out" in com:
            print()
            print("You open the door to the lab and step out into a small area that leads to a number of rooms")
            print("You can see a hallway in view. The IT Lab is next to you and the men's and")
            print("women's bathrooms are in sight.")
            stack.push('csLab()')
            outsideCsLab()
        elif "cs lab" in com:
            print("You are already in the CS Lab...")
        elif "look around" in com:
            if key:
                print("Computers line the walls around the room.")
                print("In the middle of the room there is a guinea pig cage on a table.")
            else:
                print("Computers line the walls around the room.")
                print("In the middle of the room there is a guinea pig cage on a table.")
                print("Something seems to be on the table by the cage.")
        elif "computer" in com:
            while True:
                a = input("Do you want to log in?: ").lower()
                if "y" in a:
                    username = input("Username: ").lower()
                    password = input("Password: ").lower()
                    print("You have logged in as %s." %(username))
                    break
                if "n" in a:
                    print("You left the computer alone.")
                    break
                else:
                    print("I don't understand your decision...")
        elif "table" in com:
            if key:
                print("You examine the table to find a note sitting there.")
            else:
                print("You examine the table to find a key and a note sitting there.")
        elif "cage" in com:
            print("You take a closer look at the cage and realize that the door is broken.")
        elif "door" in com:
            print("You take a closer look at the door and see that one of the hinges is missing.")
        elif "hinge" in com:
            print("One of the hinges is missing.")
        elif ("examine" in com and "key" in com) or ("look" in com and "key" in com):
            if key:
                print("You take the key out of your bag and inspect it. The key appears to be worn from repeated use.")
            else:
                print("You look at the key on the table and realize it could open one of the doors in Resch.")
        elif ("take" in com and "key" in com) or ("get" in com and "key" in com) or ("pick up" in com and "key" in com):
            if key:
                print("The key is already in your pocket...")
            else:
                print("You pick up the key and put it in your pocket.")
                inv.append("Jim's Key")
                print("*Jim's Key added to inventory*")
        elif ("take" in com and "note" in com) or ("pick up" in com and "note" in com):
            print("You don't need the note for anything...")
        elif "note" in com:
            print("You pick up the crinkled note and read the message:\n")
            print("I remembered to feed the Guinea pig")
            print("                         -Dr. R")
        elif "examine" in com:
            print("Examine what?")
        else:
            print("I do not understand your command.")


def itLab():
    while True:
        if "Kool-Aid" in inv:
            kool=True
        else:
            kool=False
        if "hingeused" in dummy:
            used=True
        else:
            used=False
        if "Someone's Hat" in inv:
            hat=True
        else:
            hat=False
        if 'hatlost' in dummy:
            lost=True
        else:
            lost=False
        com = input('>').lower()
        if "Hinge" in inv:
            hinge=True
        else:
            hinge=False
        if "Flashlight" in inv:
            light=True
        else:
            light=False
        if "computerassembled" in dummy:
            assembled=True
        else:
            assembled=False
        if len(com.strip()) <= 0:
            continue
        elif "table" in com or "middle" in com:
            if hat and light and not assembled:
                print("You look at the tables and see that one of them is covered in tools. Another table has a rather hastily disassembled computer.")
            elif lost and light and not assembled:
                print("You look at the tables and see that one of them is covered in tools. Another table has a rather hastily disassembled computer.")
            elif light and not hat and not assembled:
                print("You look at the tables and see that one of them is covered in tools while the other has a")
                print("familiar looking hat on it. Another table has a rather hastily disassembled computer.")
            elif hat and not light or lost and not light and not assembled:
                print("You look at the tables and see that one of them is covered in tools. There is a flashlight")
                print("by the tools. Another table has a rather hastily disassembled computer.")
                
            elif hat and light and assembled:
                print("You look at the tables and see that one of them is covered in tools. Another table has the assembled computer.")
            elif lost and light and assembled:
                print("You look at the tables and see that one of them is covered in tools. Another table has the assembled computer.")
            elif light and not hat and assembled:
                print("You look at the tables and see that one of them is covered in tools while the other has a")
                print("familiar looking hat on it. Another table has the assembled computer.")
            elif hat or lost and not light and assembled:
                print("You look at the tables and see that one of them is covered in tools. There is a flashlight")
                print("by the tools. Another table has the assembled computer.")
            elif not hat and not light and assembled:
                print("You look at the tables and see that one of them is covered")
                print("in tools while the other has a familiar looking hat on it. There is a flashlight by the tools.")
                print("Another table has the assembled computer.") 
            else:
                print("You look at the tables and see that one of them is covered")
                print("in tools while the other has a familiar looking hat on it. There is a flashlight by the tools.")
                print("Another table has a rather hastily disassembled computer.")
        elif "map" in com:
            print("You take out a map from your bag and look at it:\n")
            reschMapIT()
        elif "inv" in com or "bag" in com:
            bag()
        elif "drink" in com:
            if kool:
                print("You take a Kool-Aid out of the cooler and you take a drink and you begin")
                print("to feel fuzzy. The office begins to fade away eventually leading to complete darkness.....")
                print()
                print()
                print()
                print("..............")
                print("..............")
                print("..............\n")
                print("You begin to wake up and you realise that you are back where you started, in the CS Lab...")
                print("Bag empty...You have no idea what just happened...\n")
                del inv[:]
                del dummy[:]
                csLab()
            else:
                print("You never took a Kool-Aid from Jim's Office...")
        elif "leave" in com or "back" in com or "exit" in com or "out" in com:
            print("You open the door and step out of the IT Lab. You can see the hallway.")
            print("the CS Lab is beside you and the men's and women's bathrooms are straight ahead.")
            stack.push('itLab()')
            outsideCsLab()
        elif "it lab" in com:
            print("You are already in the IT Lab...")
        elif "help" in com:
            helpMe()
        elif "look around" in com:
            print("There are computers strewn everywhere and there are a couple of tables in the middle of the room.")
        elif ("pick" in com and "up" in com and "light" in com) or ("take" in com and "light" in com) or ("get" in com and "light" in com):
            if light:
                print("You already put the light in your bag")
                while True:
                    a = input("Do you want to put it back?: ").strip().lower()
                    if "y" in a:
                        inv.remove("Flashlight")
                        print("You put the Flashlight back on the table.")
                        print("You have lost an item: Flashlight")
                        break
                    elif "n" in a:
                        print("You leave the Flashlight in your bag.")
                        break
                    elif "y" not in a and "n" not in a:
                        print("I don't understand what you want me to do...")
            else:
                print("You put the Flashlight in your bag.")
                inv.append("Flashlight")
                print("*Flashlight added to inventory*")            
        elif ("pick" in com and "up" in com and "hat" in com) or ("take" in com and "hat" in com) or ("get" in com and "hat" in com):
            if hat:
                print("You already put the hat in your bag")
                while True:
                    a = input("Do you want to put it back?: ").strip().lower()
                    if "y" in a:
                        inv.remove("Someone's Hat")
                        print("You put the hat back on the table.")
                        break
                    elif "n" in a:
                        print("You leave the hat in your bag.")
                        break
                    elif "y" not in a and "n" not in a:
                        print("I don't understand what you want me to do...")
            elif lost:
                print("You gave the hat to Austin...")
            else:
                print("You put the hat in your bag.")
                inv.append("Someone's Hat")
                print("*Someone's Hat added to inventory*")
        elif "put" in com and "on" in com and "hat" in com or "wear" in com and "hat" in com:
            if hat:
                print("You take the hat out of your bag and put it on. You are not much of a hat guy so you put it")
                print("back in your bag soon after.")
            elif lost:
                print("You don't have the hat anymore... You gave it back to Austin.")
            else:
                print("You take the hat off the table and put it on. You start to wonder if the owner has lice so after a couple minutes")
                print("you take the hat off and put it back on the table to avoid further risk.")
        elif "hat" in com:
            if hat:
                print("You take the hat out of your bag and stare at it. You can't")
                print("seem to remember who wears this familiar looking ball cap")
                print("that you picked up.")
            elif lost:
                print("Austin has the hat.")
            else:
                print("It is just a regular old hat� Something people would wear")
                print("from time to time.")
        elif "take" in com and "tools" in com or "pick up" in com and "tools" in com:
            print("You don't need those tools for anything...")
        elif "tools" in com:
            if hinge or used:
                print("You fumble around the pile of tools and notice nothing of much importance.")
            else:
                print("You fumble around the pile of tools on the table and notice a peculiar")
                print("looking object. It is the hinge. Someone was fixing it.")
        elif "fix" in com and "hinge" in com:
            if not used:
                print("It's already fixed...")
            elif used:
                print("It's back on the cage door...")
        elif "assemble" in com or "fix" in com:
            if not assembled:
                itActivity()
                dummy.append('computerassembled')
            else:
                print("The computer is already assembled...")
        elif "computer" in com:
            if not assembled:
                print("You can see computers everywhere. Functioning computers are along the walls and a disassembled computer sits on")
                print("one of the tables.")
            else:
                print("You can see computers everywhere. Functioning computers are along the walls and an assembled computer sits on")
                print("one of the tables.")
        elif "log" in com:
            while True:
                a = input("Do you want to log in?: ").lower()
                if a == "yes" or a== "y":
                    username = input("Username: ").lower()
                    password = input("Password: ").lower()
                    print("You have logged in as %s." %(username))
                    break
                if a == "no" or a == "n":
                    print("You left the computer alone.")
                    break
                else:
                    print("I don't understand your decision...")
        elif "take" in com and "hinge" in com or "pick up" in com and "hinge" in com or "get" in com and "hinge" in com:
            if hinge:
                print("The hinge is already in your bag")
            elif used:
                print("You already took the hinge and fixed the door.")
            else:
                inv.append('Hinge')
                print("You took the hinge and put it in your bag")
                print("*Hinge added to inventory*")
        elif "hinge" in com:
            if hinge:
                print("You take the hinge out of your bag and inspect it. It's broken...")
            else:
                print("You pick it up and see that it's broken.")
        else:
            print("I don't understand what you are saying...")
        

def csLab():
    while True:
        if "Kool-Aid" in inv:
            kool=True
        else:
            kool=False
        com=input('>').lower()
        if "Jim's Key" in inv:
            key=True
        else:
            key=False
        if "Hinge" in inv:
            hinge=True
        else:
            hinge=False
        if "Guinea Pig" in inv:
            pig=True
        else:
            pig=False
        if "guineapighome" in dummy:
            home=True
        else:
            home=False
        if "hingeused" in dummy:
            used=True
        else:
            used=False
        if "help" in com:
            helpMe()
        elif "map" in com:
            print("You take out a map from your bag and look at it:\n")
            reschMapCS()
        elif "drink" in com:
            if kool:
                print("You take a Kool-Aid out of the cooler and you take a drink and you begin")
                print("to feel fuzzy. The office begins to fade away eventually leading to complete darkness.....")
                print()
                print()
                print()
                print("..............")
                print("..............")
                print("..............\n")
                print("You begin to wake up and you realise that you are back where you started, in the CS Lab...")
                print("Bag empty...You have no idea what just happened...\n")
                del inv[:]
                del dummy[:]
                csLab()
            else:
                print("You never took a Kool-Aid from Jim's Office...")
        elif "pig" in com and "back" in com or "pig" in com and "put" in com:
            if home:
                print("The CSIT Guinea Pig is already back in its cage. It looks mad...")
            elif pig and used and not home:
                print("You take the squirming Guinea Pig out of your arms and throw it back in the cage and close the door.")
                print("Guinea Pig has left the party")
                inv.remove('Guinea Pig')
                dummy.append('guineapighome')
            elif pig:
                print("You need to fix the door before putting the Guinea Pig back. It will run away again if you don't.")
            else:
                print("You don't have a Guinea Pig to put back silly.")
        elif "leave" in com or "exit" in com or "back" in com or "out" in com:
            print("You open the door to the lab and step out into a small area that leads to a number of rooms")
            print("You can see a hallway right ahead of you. The IT Lab is next to you and the men's and")
            print("women's bathrooms are in sight.")
            stack.push('csLab()')
            outsideCsLab()
        elif "cs lab" in com:
            print("You are already in the CS Lab...")
        elif "inv" in com or "bag" in com:
            bag()
        elif "look around" in com:
            if key:
                print("Computers line the walls around the room.")
                print("In the middle of the room there is a guinea pig cage on a table.")
            else:
                print("Computers line the walls around the room.")
                print("In the middle of the room there is a guinea pig cage on a table.")
                print("Something seems to be on the table by the cage.")
        elif "computer" in com:
            while True:
                a = input("Do you want to log in?: ").lower()
                if "y" in a:
                    username = input("Username: ").lower()
                    password = input("Password: ").lower()
                    print("You have logged in as %s." %(username))
                    break
                if "n" in a:
                    print("You left the computer alone.")
                    break
                else:
                    print("I don't understand your decision...")
        elif "table" in com:
            if key:
                print("You examine the table to find a note sitting there.")
            else:
                print("You examine the table to find a key and a note sitting there.")
        elif "cage" in com:
            if home and used:
                print("The cage is intact and the pig is running around in circles.")
            elif used:
                print("The cage is intact, but there is not Guinea Pig in the cage.")
            else:
                print("You take a closer look at the cage and realize that the door is broken.")
        elif "door" in com and "fix" in com:
            if hinge:
                print("You take the hinge out of your bag and put it back on the cage door.")
                print("The door seems to work fine now.")
                inv.remove('Hinge')
                dummy.append('hingeused')
                print("You have lost an item: Hinge")
            else:
                print("One of the hinges is missing. You can probably fix the door if you found the other hinge...")
        elif "door" in com:
            print("You take a closer look at the door and see that one of the hinges is missing.")
        elif "key" in com and "examine" in com or "look at" in com and "key" in com:
            if key:
                print("You take the key out of your bag and inspect it. The key appears to be worn from repeated use.")
            else:
                print("You look at the key on the table and realize it could open one of the doors in Resch.")
        elif "key" in com:
            if key:
                print("The key is already in your pocket...")
            else:
                print("You pick up the key and put it in your pocket.")
                inv.append("Jim's Key")
                print("*Jim's Key added to inventory*")
        elif "take" in com and "note" in com or "pick up" in com and "note" in com:
            print("You don't need the note for anything...")
        elif "note" in com:
            print("You pick up the crinkled note and read the message:\n")
            print("I remembered to feed the Guinea pig")
            print("                         -Dr. R")
        elif "examine" in com:
            print("examine what?")
        else:
            print("What are you trying to tell me?")

def womenBathroom():
    if "Kool-Aid" in inv:
        kool=True
    else:
        kool=False
    if data['gender'] == "male" or data['gender'] == "m":
        print("You can't go into the women's bathroom. You need to be a female to enter or at least look like one.\n")
        print("You turn around and the men's bathroom is directly in front of you")
        print("The IT Lab is to the northeast and the CS Lab is by the IT Lab. You can also see the hallway.")
        outsideCsLab()
    else:
        print("You are now in the women's bathroom. No one seems to be in there at the moment.")
    while True:
        com = input('>').lower()
        if len(com.strip()) <= 0:
            continue
        elif "leave" in com or "exit" in com or "back" in com or "out" in com:
            print("You step out of the women's bathroom. The men's bathroom is directly in front of you")
            print("and the IT Lab is to the northeast. The CS Lab is by IT Lab. You can also see the hallway.")
            stack.push('womenBathroom()')
            outsideCsLab()
        elif "inv" in com or "bag" in com:
            bag()
        elif "drink" in com:
            if kool:
                print("You take a Kool-Aid out of the cooler and you take a drink and you begin")
                print("to feel fuzzy. The office begins to fade away eventually leading to complete darkness.....")
                print()
                print()
                print()
                print("..............")
                print("..............")
                print("..............\n")
                print("You begin to wake up and you realise that you are back where you started, in the CS Lab...")
                print("Bag empty...You have no idea what just happened...\n")
                del inv[:]
                del dummy[:]
                csLab()
            else:
                print("You never took a Kool-Aid from Jim's Office...")
        elif "stall" in com and "examine" in com or "look" in com and "stall" in com:
            print("You look at one of the stalls and notice that someone is in one of them.")
        elif "wom" in com or "girl" in com:
            print("You are already in the Womens Bathroom.")
        elif "stall" in com:
            print("You walk to the stall and slowly open it and lo and behold there was a goat.")
        elif "help" in com:
            helpMe()
        elif "look" in com and "around" in com:
            print("You look around to see stalls and sinks...")
        elif "pick" in com and "up" in com:
            print("You can't really pick that up...")
        elif "wash" in com or ("use" in com and "sink" in com):
            print("You go to a sink and wash your hands. You feel a bit more cleaner than before.")
        elif "sink" in com:
            print("It's just a regular old sink. You can use it to wash your hands.")
        elif "use" in com and "toilet" in com or "use" in com and "urinal" in com:
            print("You don't really have the need to do that right now...")
        elif "map" in com:
            print("You take out a map from your bag and look at it:\n")
            reschMapWomen()
        else:
            print("I don't understand what you want me to do...")


def menBathroom():
    if "Kool-Aid" in inv:
        kool=True
    else:
        kool=False
    if data['gender'] == "female" or data['gender'] == "f":
        print("You can't go into the men's bathroom. You need to be a male to enter or at least look like one.\n")
        print("You turn around and the women's bathroom is directly in front of you")
        print("The IT Lab is to the northeast and the CS Lab is by the IT Lab. You can also see the hallway.")
        outsideCsLab()
    else:
        print("You are now in the men's bathroom. You can see stalls, sinks, and urinals.")
    while True:
        com = input('>').lower()
        if len(com.strip()) <= 0:
            continue
        elif "stall" in com and "examine" in com or "look" in com and "stall" in com:
            print("You look at one of the stalls and notice that someone is in one of them.")
        elif "drink" in com:
            if kool:
                print("You take a Kool-Aid out of the cooler and you take a drink and you begin")
                print("to feel fuzzy. The office begins to fade away eventually leading to complete darkness.....")
                print()
                print()
                print()
                print("..............")
                print("..............")
                print("..............\n")
                print("You begin to wake up and you realise that you are back where you started, in the CS Lab...")
                print("Bag empty...You have no idea what just happened...\n")
                del inv[:]
                del dummy[:]
                csLab()
            else:
                print("You never took a Kool-Aid from Jim's Office...")
        elif "inv" in com or "bag" in com:
            bag()
        elif "men" in com or "guy" in com:
            print("You are already in the Mens Restroom.")
        elif "stall" in com:
            print("You walk to the stall and slowly open it and lo and behold there was a goat.")
        elif "map" in com:
            print("You take out a map from your bag and look at it:\n")
            reschMapMen()
        elif "help" in com:
            helpMe()
        elif "look" in com and "around" in com:
            print("You look around to see stalls, sinks, and urinals...")
        elif "use" in com and "toilet" in com or "use" in com and "urinal" in com:
            print("You don't really have the need to do that right now...")
        elif "pick" in com and "up" in com:
            print("You can't really pick that up...")
        elif "leave" in com or "exit" in com or "back" in com or "out" in com:
            print("You step out of the men's bathroom. The women's bathroom is directly in front of you")
            print("and the IT Lab is to the northeast. The CS Lab is by the IT Lab. You can also see the hallway")
            stack.push('menBathroom()')
            outsideCsLab()
        elif "wash" in com or ("use" in com and "sink" in com):
            print("You go to a sink and wash your hands. You feel a bit more cleaner than before.")
        elif "sink" in com:
            print("It's just a regular old sink. You can use it to wash your hands.")
        else:
            print("What do you want to do???")

def jimOffice():
    if "Jim's Key" in inv:
        key=True
    else:
        key=False
    if not key:
        print("You reach your hand out to open the door to Jim's office, but it is locked. You need a key to get in. You remember vaguely")
        print("that you saw something in the CS Lab...")
        hallway()
    else:
        print("You reach your hand out to open the door to Jim's office, but it is locked...")
        while True:
            if "Kool-Aid" in inv:
                koolaid=True
            else:
                koolaid=False
            a = input("Do you want to use Jim's key?: ").strip()
            if "n" in a:
                print("You did not use the key.")
                stack.push('jimOffice()')
                hallway()
            elif "y" in a :
                print("You take Jim's key out of your bag and put it in the lock. You turn the key and the lock clicks open.\n")
                print("You are standing in Jim�s office. Papers and books are seen in piles on some tables. There is a")
                print("bright green cooler beside the door. A computer sits conspicuously on a table.")
                while True:
                    if 'jimcodesolved' in dummy:
                        solved = True
                    else:
                        solved = False
                    com=input('>').lower()
                    if "take" in com and "cooler" in com or "get" in com and "cooler" in com or "pick" in com and "cooler" in com:
                        print("You try stuffing it in your bag but it's too big...")
                    elif "cooler" in com:
                        print("You look inside the cooler and there are some suspicious looking Kool-Aid juice packs inside.")
                    elif "inv" in com or "bag" in com:
                        bag()
                    elif "take" in com and "kool" in com or "get" in com and "kool" in com or "pick" in com and "kool" in com:
                        print("You take the Kool-Aid and put it in your bag")
                        inv.append("Kool-Aid")
                        print("*Kool-Aid added to inventory*")
                    elif "examine" in com and "kool" in com:
                        if koolaid:
                            print("You take the Kool-Aid out of your bag and look at it. It looks very delicious.")
                        else:
                            print("You open the cooler and pick up one of the packs. It looks quite delicious...")
                    elif "drink" in com:
                        print("You take a Kool-Aid out of the cooler and you take a drink and you begin")
                        print("to feel fuzzy. The office begins to fade away eventually leading to complete darkness.....")
                        print()
                        print()
                        print()
                        print("..............")
                        print("..............")
                        print("..............\n")
                        print("You begin to wake up and you realise that you are back where you started, in the CS Lab...")
                        print("Bag empty...You have no idea what just happened...\n")
                        del inv[:]
                        del dummy[:]
                        csLab()
                    elif "jim" in com and "office" in com:
                        print("You are already in Jim's Office.")
                    elif "look" in com and "around" in com:
                        print("Papers and books are seen in piles on some tables. There is a")
                        print("bright green cooler beside the door. Jim's computer is turned on.")
                    elif "map" in com:
                        print("You take out a map from your bag and look at it:\n")
                        reschMapJim()
                    elif "table" in com:
                        print("Books about Python and HTML are all over the table and Jim's computer is also in view.")
                    elif "computer" in com:
                        if not solved:
                            jimActivity()
                            dummy.append('jimcodesolved')
                        else:
                            print("Jim's computer still appears to be logged in. The CSIT Guinea Pig Feeding Schedule is still displayed:\n")
                            print("GUINEA PIG FEEDING SCHEDULE")
                            print(" --------------------------")
                            print("|Date     | Time   | Name  |")
                            print("|--------------------------|")
                            print("|5/6/2012 | 5:00pm | Jim   |")
                            print("|5/7/2012 | 5:00pm | Kevin |")
                            print("|5/8/2012 | 5:00pm | Ron   |")
                            print(" -------------------------- ")
##                    elif "schedule" in com and "take" in com or "schedule" in com and "get" in com or "schedule" in com and "pick" in com:
##                        print("It's not a good idea to take stuff from a professors office without asking...")
##                    elif "schedule" in com:
##                        print("You pick up the schedule and read it:\n")
##                        print("GUINEA PIG FEEDING SCHEDULE")
##                        print(" --------------------------")
##                        print("|Date     | Time   | Name  |")
##                        print("|--------------------------|")
##                        print("|5/6/2012 | 5:00pm | Jim   |")
##                        print("|5/7/2012 | 5:00pm | Kevin |")
##                        print("|5/8/2012 | 5:00pm | Ron   |")
##                        print(" -------------------------- ")
                    elif "book" in com and "take" in com or "book" in com and "get" in com or "book" in com and "pick" in com:
                        print("It's not a good idea to take stuff from a professors office without asking...")
                    elif "book" in com:
                        print("You open up a one of the books and start reading... You instantly become bored and put it back down.")
                    elif "back" in com or "leave" in com or "exit" in com or "out" in com:
                        stack.push('jimOffice()')
                        janitor()
                    else:
                        print("I don't understand what you are saying")
            else:
                print("I don't understand what you want me to do... What did you say again?:")

def janitor():
    if "Janitor's Key" in inv:
        key=True
    else:
        key=False
    if key:
        print("You step out of Jim's office and lock the door behind you. You are now in the hallway.")
        hallway()
    else:
        print("You walk out of Jim�s office and lock the door behind you. Suddenly the Janitor runs into you.")
        print("You tell him about your ordeal and out of pity, he hands you the master key to the rest of the offices.")
        inv.append("Janitor's Key")
        print()
        print("The Janitor walks away leaving you alone once again in the hallway.")
        hallway()

def ruOffice():
    if "Kool-Aid" in inv:
        kool=True
    else:
        kool=False
    if "Janitor's Key" in inv:
        key=True
    else:
        key=False
    if not key:
        print("You reach your hand out to open the door to Ru's office, but it is locked. You need a key to get in. You need")
        print("a key to get in...")
        hallway()
    else:
        print("You reach your hand out to open the door to Ru's office, but it is locked...")
        while True:   
            a = input("Do you want to use the Janitor's Key?: ").strip()
            if "n" in a:
                print("You did not use the key.")
                stack.push('ruOffice()')
                hallway()
            elif "y" in a :
                print("You take the Janitor's Key out of your bag and put it in the lock. You turn the key and the lock clicks open.\n")
                print("You are standing in Ru�s office. It looks quite empty. A random trebuchet sits in the front of the office and")
                print("there is a table with a bunch of books on it.") 
                while True:
                    com=input('>').lower()
                    if "look" in com and "around" in com:
                        print("The office looks quite empty. A random trebuchet sits in the front of the office and something")
                        print("seems somewhat hidden on a desk.")
                    elif "drink" in com:
                        if kool:
                            print("You take a Kool-Aid out of the cooler and you take a drink and you begin")
                            print("to feel fuzzy. The office begins to fade away eventually leading to complete darkness.....")
                            print()
                            print()
                            print()
                            print("..............")
                            print("..............")
                            print("..............\n")
                            print("You begin to wake up and you realise that you are back where you started, in the CS Lab...")
                            print("Bag empty...You have no idea what just happened...\n")
                            del inv[:]
                            del dummy[:]
                            csLab()
                        else:
                            print("You never took a Kool-Aid from Jim's Office...")
                    elif "inv" in com or "bag" in com:
                        bag()
                    elif "map" in com:
                        print("You take out a map from your bag and look at it:\n")
                        reschMapRu()
                    elif "ru" in com and "office" in com:
                        print("You are already in Ru's Office.")
                    elif "trebuchet" in com:
                        print("You take a closer look at the trebuchet, but nothing seems too conspicuous about it.")
                    elif "desk" in com or "table" in com:
                        print("You take a closer look at the desk and see many books about Unix, Linux, and Physics. You notice")
                        print("something hidden under the books.")
                    elif "under" in com and "book" in com:
                        print("You take a closer look at what was under the books and see that it is a diary.")
                    elif "take" in com and "diary" in com or "get" in com and "diary" in com or "pick" in com and "diary" in com:
                        print("Although tempting, it is not a good idea to take someone's diary.")
                    elif "book" in com and "take" in com or "book" in com and "get" in com or "book" in com and "pick" in com:
                        print("It's not a good idea to take stuff from a professors office without asking...")
                    elif "book" in com:
                        print("You pick up one of the books and it happens to be about physics. You read something on the lines of")
                        print("'Gmn = -(8pG/c2)Tmn'. You suddenly feel smarter...")
                    elif "diary" in com:
                        print("You open the diary and read the latest entry:\n")
                        print("May 8, 2012\n")
                        print("Day by day I am saddened that I cannot be near the beloved")
                        print("CSIT Guinea Pig. Oh how I long to hold and pet it, but my")
                        print("severe allergies to these adorable creatures prevents me from")
                        print("doing so� I cannot get my mind off of those two black beady")
                        print("eyes that are constantly staring deep into my soul as I")
                        print("teach the students about how to program in Bash and Perl�\n")
                        print("-Dr. R")
                    elif "back" in com or "leave" in com or "exit" in com or "out" in com:
                        print("You step out of Ru's office and lock the door behind you. You are now in the hallway.")
                        stack.push('ruOffice()')
                        hallway()
                    else:
                        print("I don't understand what you want me to do...")
            else:
                print("I don't understand what you want me to do... What did you say again?:")

def ronOffice():
    if "Kool-Aid" in inv:
        kool=True
    else:
        kool=False
    if "Janitor's Key" in inv:
        key=True
    else:
        key=False
    if not key:
        print("You reach your hand out to open the door to Ron's office, but it is locked. You need a key to get in...")
        hallway()
    else:
        print("You reach your hand out to open the door to Ron's office, but it is locked...")
        while True:
            a = input("Do you want to use the Janitor's Key?: ").lower()
            if "n" in a:
                print("You did not use the key.")
                stack.push('ronOffice()')
                hallway()
            elif "y" in a:
                print("You take the Janitor's Key out of your bag and put it in the lock. You turn the key and the lock clicks open.\n")
                print("You are in Ron's office. There is a comfortable looking bean bag in the corner of the room.")
                print("The place appears to be in a state of organized chaos. Papers and books are strewn all over the table.")
                print("At your feet you notice a pile of Calculus 4 assignments that have been slipped under the door.")

                while True:
                    com = input('>').lower()
                    if len(com.strip()) <= 0:
                      continue
                    elif "help" in com:
                        helpMe()
                    elif "map" in com:
                        print("You take out a map from your bag and look at it:\n")
                        reschMapRon()
                    elif "drink" in com:
                        if kool:
                            print("You take a Kool-Aid out of the cooler and you take a drink and you begin")
                            print("to feel fuzzy. The office begins to fade away eventually leading to complete darkness.....")
                            print()
                            print()
                            print()
                            print("..............")
                            print("..............")
                            print("..............\n")
                            print("You begin to wake up and you realise that you are back where you started, in the CS Lab...")
                            print("Bag empty...You have no idea what just happened...\n")
                            del inv[:]
                            del dummy[:]
                            csLab()
                        else:
                            print("You never took a Kool-Aid from Jim's Office...")
                    elif "ron" in com and "office" in com:
                        print("You are already in Ron's Office.")
                    elif "bean" in com:
                        print("The bean bag appears to be quite puffy and welcoming. You reach out to touch it and")
                        print("notice something odd. There is some kind of hair, too small for it to belong to a human,")
                        print("on the bean bag.")
                    elif "inv" in com or "bag" in com:
                        bag()
                    elif "look around" in com:
                        print("There is a comfortable looking bean bag in the corner of the room. The place appears to be")
                        print("in a state of organized chaos. Papers and books are strewn all over the table.")
                        print("At your feet you notice a pile of Calculus 4 assignments that have been slipped under the door.")
                    elif "assignment" in com and "take" in com or "assignment" in com and "get" in com or "assignment" in com and "pick" in com or "home" in com and "take" in com or "home" in com and "get" in com or "home" in com and "pick" in com:
                        print("It's not a good idea to take other peoples homework...")
                    elif "assignment" in com or "homework" in com:
                        print("You pick up the homework and look at the heading:\n")
                        print("Sam McFarlin")
                        print("Calculus IV")
                        print("March 28, 2012")
                        print("HW 11\n")
                        print("You put the assignment down and feel confused. You think to yourself: That assignment was due a month ago...")
                    elif "table" in com:
                        print("There are numerous Calculus books strewn all over the place, too complicated for a human being to")
                        print("understand. There is a noticeable piece of paper with some writing on it under one of the textbooks.")
                    elif "under" in com:
                        print("You look a bit closer and see that there is a note under the textbook.")
                    elif "book" in com and "take" in com or "book" in com and "get" in com or "book" in com and "pick" in com:
                        print("It's not a good idea to take Ron's books without asking...")
                    elif "book" in com:
                        print("You pick up one of the calculus books and turn to a random page... You read something about")
                        print("a triple integral and become overwelmed. You quickly put the book down to avoid further brain")
                        print("damage.")
                    elif "note" in com and "take" in com or "note" in com and "get" in com or "note" in com and "pick" in com:
                        print("Ron might forget about his classes if you take his note...")
                    elif "paper" in com or "note" in com:
                        print("You pick up the paper and read the contents:\n")
                        print("Remember!!!! Calculus at 9:00 in the morning and Data Structures at 11:00 in the morning...\n")
                        print("-Dr. R")
                    elif "back" in com or "leave" in com or "exit" in com:
                        print("You step out of Ron's office and lock the door behind you. You are now in the hallway.")
                        stack.push('ronOffice()')
                        hallway()
                    else:
                        print("What do you want me to do?!?!?!?!?")
            else:
                print("I don't understand what you want me to do... What did you say again?:")


def kevinOffice():
    if "Kool-Aid" in inv:
        kool=True
    else:
        kool=False
    if "Janitor's Key" in inv:
        key=True
    else:
        key=False
    if not key:
        print("You reach your hand out to open the door to Kevin's office, but it is locked. You need a key to get in...")
        hallway()
    else:
        print("You reach your hand out to open the door to Kevin's office, but it is locked...")
        while True:
            a = input("Do you want to use the Janitor's Key?: ").lower()
            if "n" in a:
                print("You did not use the key.")
                stack.push('kevinOffice()')
                hallway()
            elif "y" in a:
                print("You take the Janitor's Key out of your bag and put it in the lock. You turn the key and the lock clicks open.\n")
                print("You are standing in Kevin�s office. There is a conspicuous looking golf bag in the corner of the room and")
                print("some books and papers are on a table")
                while True:
                    com = input('>').lower()
                    if len(com.strip()) <= 0:
                      continue
                    elif "help" in com:
                        helpMe()
                    elif "inv" in com or ("bag" in com and "golf" not in com):
                        bag()
                    elif "map" in com:
                        print("You take out a map from your bag and look at it:\n")
                        reschMapKevin()
                    elif "look" in com and "around" in com:
                        print("You take a look around to see a conspicuous looking golf bag in the corner of the room and")
                        print("some books and papers on a table")
                    elif "drink" in com:
                        if kool:
                            print("You take a Kool-Aid out of the cooler and you take a drink and you begin")
                            print("to feel fuzzy. The office begins to fade away eventually leading to complete darkness.....")
                            print()
                            print()
                            print()
                            print("..............")
                            print("..............")
                            print("..............\n")
                            print("You begin to wake up and you realise that you are back where you started, in the CS Lab...")
                            print("Bag empty...You have no idea what just happened...\n")
                            del inv[:]
                            del dummy[:]
                            csLab()
                        else:
                            print("You never took a Kool-Aid from Jim's Office...")
                    elif "kevin" in com and "office" in com:
                        print("You are already in Kevin's Office.")
                    elif "golf" in com and "take" in com or "golf" in com and "get" in com or "golf" in com and "pick" in com:
                        print("That bag looks pretty expensive. Better not take it.")
                    elif "examine" in com and "club" in com or "look" in com and "club" in com:
                        print("You take a closer look at the clubs and see the various types of clubs in the bag. There are putters, drivers,")
                        print("irons, wedges, and other things you can't really explain.")
                    elif "swing" in com:
                        print("The office is too small for that...")
                    elif "golf" in com:
                        print("You approach the golf bag and take a look. You see some regular looking clubs and a pair of golfing shoes.")
                    elif "wear" in com:
                        print("You try putting them on, but they are too big for you...")
                    elif "examine" in com and "shoe" in com or "look" in com and "shoe" in com:
                        print("You pick up one of the shoes and stare at it. You see something odd on the bottom of the shoe. It looks like")
                        print("a brown pellet. It reminds you of some kind of poop...")
                    elif "table" in com:
                        print("You take a closer look at the table to see books about JAVA and also a note.")
                    elif "book" in com and "take" in com or "book" in com and "get" in com or "book" in com and "pick" in com:
                        print("It's not a good idea to take Kevin's books without asking...")
                    elif "read" in com and "book" in com:
                        print("You open up one of the books and read something about classes, objects, inheritance, and packages. You loose")
                        print("interest quickly and put the book down.")
                    elif "note" in com and "take" in com or "note" in com and "get" in com or "note" in com and "pick" in com:
                        print("It's not a good idea to take Kevin's notes. He really cherishes them.")
                    elif "note" in com and "read" in com:
                        print("You pick up the note and read what it says:\n")
                        print("Reminder: Tell Janitor about brown poop things on the FLOOR in room 103.")
                    elif "back" in com or "leave" in com or "exit" in com:
                        print("You step out of Kevin's office and lock the door behind you. You are now in the hallway.")
                        stack.push('kevinOffice()')
                        hallway()
                    else:
                        print("I don't know what you want me to do...")
            else:
                print("I don't understand what you want me to do... What did you say again?:")

def room103():
    if "Kool-Aid" in inv:
        kool=True
    else:
        kool=False
    if "Janitor's Key" in inv:
        key=True
    else:
        key=False
    if not key:
        print("You reach your hand out to open the door to Room 103 but it is locked. You need a key to get in...")
        eastHallway()
    else:
        print("You reach your hand out to open the door to Room 103, but it is locked...")
        while True:
            a = input("Do you want to use the Janitor's Key?: ").lower()
            if "n" in a:
                print("You did not use the key.")
                stack.push('room103()')
                eastHallway()
            elif "y" in a:
                print("You take the Janitor's Key out of your bag and put it in the lock. You turn the key and the lock clicks open.\n")
                print("You are now in room 103. The room is quite big and there are many tables and chairs in neat rows.")
                while True:
                    if "guineapighome" in dummy:
                        home=True
                    else:
                        home=False
                    if "guineamoved" in dummy:
                        moved=True
                    else:
                        moved=False
                    if "Guinea Pig" in inv:
                        pig=True
                    else:
                        pig=False
                    com = input('>').lower()
                    if len(com.strip()) <= 0:
                      continue
                    elif "help" in com:
                        helpMe()
                    elif "inv" in com or "bag" in com:
                        bag()
                    elif "map" in com:
                        print("You take out a map from your bag and look at it:\n")
                        reschMap103()
                    elif "drink" in com:
                        if kool:
                            print("You take a Kool-Aid out of the cooler and you take a drink and you begin")
                            print("to feel fuzzy. The office begins to fade away eventually leading to complete darkness.....")
                            print()
                            print()
                            print()
                            print("..............")
                            print("..............")
                            print("..............\n")
                            print("You begin to wake up and you realise that you are back where you started, in the CS Lab...")
                            print("Bag empty...You have no idea what just happened...\n")
                            del inv[:]
                            del dummy[:]
                            csLab()
                        else:
                            print("You never took a Kool-Aid from Jim's Office...")
                    elif "103" in com:
                        print("You are already in Room 103.")
                    elif "austin" in com:
                        print("He is in room 105...")
                    elif "floor" in com:
                        if pig or home:
                            print("There are still brown poops on the floor. The Janitor needs to do his job better...")
                        elif moved:
                            print("You stoop down and look at the floor closely. Just like Kevin's note said, there is indeed little brown")
                            print("poop pellets on the floor. As you are standing back up, you catch something moving in the corner of the room.")
                        else:
                            print("You stoop down and look at the floor closely. Just like Kevin's note said, there is indeed little brown")
                            print("poop pellets on the floor.")
                    elif "look" in com and "around" in com:
                        print("You look around to see that the room is quite big and there are many tables and chairs in neat rows.")
                    elif "corner" in com:
                        if pig or home:
                            print("The Guinea Pig was in this corner, but you already picked it up. You can also see a hole in the wall,")
                            print("which explains how the Guinea Pig got in the room when it was locked...")
                        elif moved and not home:
                            print("You walk over to the corner of the room take a closer look. It is the CSIT Guinea Pig! It is standing there")
                            print("petrified.")
                        else:
                            print("There is nothing there except for a small hole in the wall.")
                    elif "hole" in com:
                        print("You bend down to take a closer look. It's just a hole in the wall...")
                    elif "pig" in com and "take" in com or "pig" in com and "get" in com or "pig" in com and "pick" in com:
                        if pig or home:
                            print("You already picked the Guinea Pig up...")
                        elif not home and moved:
                            print("You gently pick up the Guinea Pig and place it in your arms.")
                            inv.append('Guinea Pig')
                            print("Guinea Pig has joined the party.")
                        else:
                            print("I'm not sure if there is a Guinea Pig here...")
                    elif "kick" in com and "pig" in com:
                        if moved and not home and not pig:
                            print("You boot the pig with your foot. It squealed angrily.")
                            print()
                            print()
                            print("""
           _mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm_          
         M -----------------------------------------------------------------------------------------------  M
        M    MMMMMMM             __         _      _       _      ___                    __  __      _  _     M  
       M   M:''     /M       /\ |   |__| | |_ \  /|_ |\/| |_ |\ |  |      |  | |\ | |   |  ||   |_/ |_ | \     M
       M  M::\\   //  M     /--\|__ |  | | |_  \/ |_ |  | |_ | \|  |      |__| | \| |__ |__||__ | \ |_ |_/     M                        
       M  M::  \\//   M                                                                                        M
       M  M::  //\\   M     50G -- ANIMAL ABUSE                                                                M
       M   M://.   \\M                                                                                         M 
        M    MMMMMMM                                                                                          M
         M _________________________________________________________________________________________________ M 
           -mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm-
""")
                        else:
                            print("Do whaaaaat???")
                    elif "chair" in com and "sit" in com:
                        print("You walk towards one of the chairs and sit on it. You feel quite comfortable.")
                    elif "chair" in com:
                        print("You walk towards a chair and take a closer look. Nothing appears to be out of place about it.")
                    elif "table" in com:
                        print("You walk towards the tables and stare at them. They are clean and neatly arranged. There is nothing")
                        print("much else to them.")
                    elif "back" in com or "leave" in com or "exit" in com or "east" in com:
                        print("You step out of Room 103 and lock the door behind you. You are now in the east wing of the hallway.")
                        stack.push('room103()')
                        eastHallway()
                    else:
                        print("I don't know what you are talking about.")


def room105():
    if "Kool-Aid" in inv:
        kool=True
    else:
        kool=False
    if "Janitor's Key" in inv:
        key=True
    else:
        key=False
    if not key:
        print("You reach your hand out to open the door to Room 105, but it is locked. You need a key to get in...")
        eastHallway()
    else:
        print("You reach your hand out to open the door to Room 105, but it is locked...")
        while True:
            a = input("Do you want to use the Janitor's Key?: ").lower()
            if "n" in a:
                print("You did not use the key.")
                stack.push('room105()')
                eastHallway()
            elif "y" in a:
                print("You take the Janitor's Key out of your bag and put it in the lock. You turn the key and the lock clicks open.\n")
                print("You are now in Room 105. You see tables an chairs arranged in neat rows. You also see Austin lounging on one of the")
                print("chairs with his usual smolder.")
                while True:
                    if "guineamoved" in dummy:
                        moved=True
                    else:
                        moved=False
                    if "Guinea Pig" in inv:
                        pig=True
                    else:
                        pig=False
                    if "Someone's Hat" in inv:
                        hat=True
                    else:
                        hat=False
                    if "guineapighome" in dummy:
                        home=True
                    else:
                        home=False
                    if 'hatlost' in dummy:
                        lost=True
                    else:
                        lost=False
                    com = input('>').lower()
                    if len(com.strip()) <= 0:
                      continue
                    elif "help" in com:
                        helpMe()
                    elif "inv" in com or "bag" in com:
                        bag()
                    elif "map" in com:
                        print("You take out a map from your bag and look at it:\n")
                        reschMap105()
                    elif "drink" in com:
                        if kool:
                            print("You take a Kool-Aid out of the cooler and you take a drink and you begin")
                            print("to feel fuzzy. The office begins to fade away eventually leading to complete darkness.....")
                            print()
                            print()
                            print()
                            print("..............")
                            print("..............")
                            print("..............\n")
                            print("You begin to wake up and you realise that you are back where you started, in the CS Lab...")
                            print("Bag empty...You have no idea what just happened...\n")
                            del inv[:]
                            del dummy[:]
                            csLab()
                        else:
                            print("You never took a Kool-Aid from Jim's Office...")
                    elif "back" in com or "leave" in com or "exit" in com or "east" in com:
                        print("You step out of Room 105 and lock the door behind you. You are now in the east wing of the hallway.")
                        stack.push('room105()')
                        eastHallway()
                    elif "105" in com:
                        print("You are already in Room 105.")
                    elif "chair" in com and "sit" in com:
                        print("You walk towards one of the chairs and sit on it. You feel quite comfortable.")
                    elif "chair" in com:
                        print("You walk towards a chair and take a closer look. Nothing appears to be out of place about it.")
                    elif "table" in com:
                        print("You walk towards the tables and stare at them. They are clean and neatly arranged. There is nothing")
                        print("much else to them.")
                    elif "look" in com and "around" in com:
                        print("You don't see much. All you see are tables, chairs, and Austin...")
                    elif "punch" in com and "austin" in com:
                        print("You run over and punch Austin. He doesn't look too happy...")
                    elif "austin" in com:
                        if home and lost:
                            print("You approach Austin and begin to talk with him:\n")
                            print("%s: Ok... You better tell me what's going on after all that trouble you put me through by making me" %(data['name']))
                            print("    find that pig and also your hat...\n")
                            print("Austin: Ok ok ok I admit it... It was me... Ron did feed the Guinea Pig today, but I went in later that day")
                            print("        to pet it. The hinge to the door broke when I opened the cage so I tried to fix it in the IT Lab.")
                            print("        I accidentally left my hat in there too... dang...\n")
                            print("%s: Oh wow... I thought it was Dr. Ron, but you out of all people...\n" %(data['name']))
                            print("Austin: Yea... I know... dat cray...\n")
                            print()
                            print()
                            print("""
           _mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm_          
         M -----------------------------------------------------------------------------------------------  M
        M    MMMMMMM             __         _      _       _      ___                    __  __      _  _     M  
       M   M:''     /M       /\ |   |__| | |_ \  /|_ |\/| |_ |\ |  |      |  | |\ | |   |  ||   |_/ |_ | \     M
       M  M::\\   //  M     /--\|__ |  | | |_  \/ |_ |  | |_ | \|  |      |__| | \| |__ |__||__ | \ |_ |_/     M                        
       M  M::  \\//   M                                                                                        M
       M  M::  //\\   M     50G -- CSIT GUINEA PIG SAVIOR                                                      M
       M   M://.   \\M                                                                                         M 
        M    MMMMMMM                                                                                          M
         M _________________________________________________________________________________________________ M 
           -mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm-
""")
                        elif not home and lost and not pig:
                            print("You approach Austin and begin to interrogate him:\n")
                            print("%s: Tell me what happened!!!\n" %(data['name']))
                            print("Austin: Woa woa woaaa slowww dowwn mannn. Before I tell you anything, I want you to find that Guinea Pig and put")
                            print("it back in the cage...\n")
                            print("%s: What? How come?\n" %(data['name']))
                            print("Austin: Ummm..... just because...\n")
                        elif not home and lost and pig:
                            print("You approach Austin and begin to talk to him: \n")
                            print("%s: Yo look what I have here man.\n" %(data['name']))
                            print("Austin: Maaannn I told you to put it back in the cage, not bring it to me...")
                        else:
                            print("You approach Austin and begin to talk with him:\n")
                            print("%s: Do you know anything about the Guinea Pig incident?\n" %(data['name']))
                            print("Austin: Umm perhaps. I might tell you more about it if you find my hat...\n")
                            while True:
                                a = input("Do you have my hat?: ").lower()
                                if 'y' in a:
                                    if hat:
                                        print("You take the hat out of your bag and give it to Austin.")
                                        inv.remove("Someone's Hat")
                                        dummy.append('hatlost')
                                        print("You have lost an item: Someone's Hat")
                                        break
                                    else:
                                        print("Austin: Hey man, I know you don't have it. Go look harder.\n")
                                        break
                                elif 'n' in a:
                                    print("Austin: Well, you better go find it.\n")
                                    break
                                else:
                                    print("Austin: I'm going to ask you again...\n")
                                    pass

                    else:
                        print("I don't know what you are saying.")

stack = Stack()    
data={}
inv=[]
dummy=[]
print("""
                 $$$$$$\                                                      $$\     $$\                           $$\           
                $$  __$$\                                                     $$ |    $$ |                          \__|          
                $$ /  \__|$$\   $$\ $$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$$\ $$$$$$\   $$$$$$$\   $$$$$$\   $$$$$$$\ $$\  $$$$$$\  
                \$$$$$$\  $$ |  $$ |$$  __$$\  \____$$\ $$  __$$\ $$  _____|\_$$  _|  $$  __$$\ $$  __$$\ $$  _____|$$ | \____$$\ 
                 \____$$\ $$ |  $$ |$$ |  $$ | $$$$$$$ |$$$$$$$$ |\$$$$$$\    $$ |    $$ |  $$ |$$$$$$$$ |\$$$$$$\  $$ | $$$$$$$ |
                $$\   $$ |$$ |  $$ |$$ |  $$ |$$  __$$ |$$   ____| \____$$\   $$ |$$\ $$ |  $$ |$$   ____| \____$$\ $$ |$$  __$$ |
                \$$$$$$  |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |\$$$$$$$\ $$$$$$$  |  \$$$$  |$$ |  $$ |\$$$$$$$\ $$$$$$$  |$$ |\$$$$$$$ |
                 \______/  \____$$ |\__|  \__| \_______| \_______|\_______/    \____/ \__|  \__| \_______|\_______/ \__| \_______|�
                          $$\   $$ |                                                                                              
                          \$$$$$$  |                                                                                              
                           \______/                                                                                               
                                                                                                                        
                                                                Welcome to Syn�sthesia
                                                                A samyoung production
                                                                   copyright 2012                        


                                                                                                
                                                                   ,::~=~~=~=~:~~=~~:                                
                                                               .$ZOZ=~~~==~~~=:,:~~~~:,,...                             
                                                             .,88O8ZO$?++====,.,.,==++=?+?=..                           
                                                           .,:$$OOO8O$I7II?++:,,.,~??I7IO$ZZO.                          
                                                         ..~7I77I7$ZOOZ7II???+:,,,,:?I$77$$ZO=                          
                                                        .,:$O$$ZOOO8Z$Z$7I??+=:,:,,,~?7$$Z$Z$:                     
                                                       .,:~~OODDDNOZOZZ$7I?++=,:,,,,,??$O8Z                    
                                                     ..::~~=~$888DDO8DOZ$7$???,,:,,,,:?ZZ7,                     
                                                    .::~~==~~?I77ZOOOO8Z7NMM7?:,:,:,::=NOO$=                       
                                                   ,:::~==~~~?7$$ZZO$7?I?MDD8+,:::::::,=7$$7:                        
                                                  .:::~+==~~=+I7$$II?+??=+++:,,:::::::::,==+?..                         
                                                 .::~~==+=~~=?I+~:~:::=~~:,.,,,::::::~::,.,:+~.                         
                                                  ::~:===~~~=+~~~~::,,::,,::,:~~::::::::::::~=.
                                                 ,::~~====~~=+=~~~::::,,,:~:~=:,~~~~~~~::~~::=,
                                                 :~~~====~==~=+~~:::::,::,,,,~:~~++I=++:~~:::=:
                                                 ,~~~~==+===~+=:=::::::::,::::~=+IZ????=~~~~~=~                      
                                                 ,~=~~========~+:~::::::~::,::~==?I???=~~~~~==: 
                                                 .~~~~~=+++====~~~:::::::::,::~~=+I7I=~~~~~=++,        
                                                 .:~~~~=+++=+++++=~~::::::::::~=~=++=~~====??=,                 
                                                 .~~=~~~=++++++???+===~~:~~~~~~~==~~===++?II?+                     
                                                  :===~~=++++++????I???++====++???+???I7IIII+,
                                                  ,~===~===+++?+?????I?II??+??I??III777$$$$I+                       
                                                  .,=+++===+++???II?77777III7I777I77$ZZZ$7I=,..                         
                                                 ...:=+?===++????IIII7$77777777$7$$ZOD8Z$7I,...                         
                                                 ..,:=?=I77?++???I?777$$ZODOZZZZZODNNND8Z7+,....                        
                                                   ..,:~?$Z$+=+?III777$8$O88ND88DMMMNND88$~:,,....                      
                                                      ...,,::~=+?I7$Z8I8IO$Z8MMMMMMMN8MDOZOI~:,,.....                   
                                                            .......,,,:::~==+?IIIIIII??++=~:,,.....                        





""")
while True:
    name=input('Please enter your name.\n>').strip()
    if len(name)==0:
        print("You did not enter a name...")
    else:
        a = input("Are you sure your name is %s?: " %(name)).lower()
        if "y" in a:
            break
        if "n" in a:
            pass
        else:
            print("I don't know what you are saying...")
            pass
while True:
    print()
    gender=input('Please enter your gender.\n>').lower()
    if gender!='male' and gender!='female' and gender!="m" and gender!="f":
        print("Are you sure you are a '%s'?" %(gender))
    else:
        break


data['name']=name
data['gender']=gender
print("                                                                     Thank you.")
print("                                                 If you need suggestions for commands, enter HELP.")
print("                                                 To view your inventory at any time, enter INV")
print("                                                                       Enjoy!\n")
input("                                                            Please press ENTER to begin\n\n")
start()
