print("""You enter a dark room with two doors.
Do you go through door 1, door 2, or door 3?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":

    print("You are overcome with a mad inspiration. You decide to offer to paint the bear's portrait.")
    print("The bear responds by (a) growling or (b) sniffing you. Which is it?")

    response = input("> ")

    if response == "growling":
        print("Run!")
    elif response == "sniffing":
        print("Good job. Get out your paintbox.")
    else:
        print("I have no idea what to say to you, you rebel.")

else:
    print("You stumble around and fall on a knife and die. Good job!")
