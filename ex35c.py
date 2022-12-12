# I don't know what exit is
from sys import exit

# function called gold_room. I guess functions don't need paramaters
def gold_room():
    print("This room is full of gold. How many pounds do you take?")

# assigning user input to variable called choice
# if loop. If user inputs 0 or 1, their input is converted to an integer and
# assigned to variable called how_much
    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
# if user input contains no 0 or 1, dead happens. What is dead? a method?
# I think dead() is another form of exit() where the parameter inside the ()
# can be any error message and you can write your own as a string inside " ".
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")

# what is exit function?
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

# True is referring to itself making an infinite loop
    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print('You can go through it now. To do so, type "open door".')
            # I DON'T UNDERSTAND THIS WHOLE BEAR_MOVED STUFF, EXPECIALLY THE ELIF BELOW
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
# what is start function?
        start()
    elif "head" in choice:
        dead("Well that was tasty!")

# sends you back to the beginning of the cthulhu_room segment I think. Kind of makes a loop
    else:
        print('You notice a door with a sign on it that says "Tea Party".')
        teaparty_room()

def teaparty_room():
    print("A table is set for a tea party. A fairy hands you a cup. Do you join her?")
    choice = input("> ")
    if "Y" in choice:
        dead("You sip the tea. It is poisoned. You die.")
    elif "N" in choice:
        print("You are ejected from the Tea Party room back into the Cthulhu Room.")
        cthulhu_room()
    else:
        dead("You fail at tea parties. Good job.")

# what is why parameter?
def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

# running the start() function:
start()
