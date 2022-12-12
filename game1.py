





def start():
    print("""
You wake up one day with a smashing headache.\nYou look in the mirror, and a haggard stranger squints back. Groaning, you \n
    \t(a)	go to the kitchen for a glass of water. \n
    \t(b)	bang your head against the wall. \n
    \t(c)	crawl back in bed, pulling the covers over your face. \n
(Make your move by typing a single lowercase letter.)
    """)
    choice = input("> ")

    if choice == "a":
        kitchen()

    elif choice == "b":
        wall()

    elif choice == "c":
        bed()

    elif choice == "A" or choice == "B" or choice == "C":
        print('Turn off caps lock and try again! Enter "ok" to continue.')
        response = input("> ")

        if response == "ok":
            start()

        else:
            dead('You did not enter "ok". GAME OVER.')

    else:
        print("""
        Please review your options and try again. This is a game, not real life.
        Therefore, your options are limited. Enter 'ok' to continue.
        """)
        response = input("> ")

        if response == "ok":
            start()

        else:
            dead('You did not enter "ok". GAME OVER.')



def kitchen():
    print("""
    You grab a glass from the cupboard and turn on the tap.
    Instead of a stream of water, a wispy little sprite wriggles from the faucet.
    She floats across the counter and perches on the edge, quivering slightly.
    "Hey you!" she says in a startlingly bright, nasal voice. “Did you know?" she continued.
    "Creativity can SAVE YOUR LIFE!"" \n
    Suddenly the sprite shape shifts into an ugly troll.
    The troll pulls out a custom, shiny red Glock handgun and points it at your head.
    When he opens his mouth, the sprite’s nasal tone floats incongruously
    from his be-bearded lips. “You will die if you don’t perform an act of
    creativity at this very moment. Do something, quick!” \n
    What is the first thing you think of? Type it now:
    """)

def wall():
    print("""
    Your headache becomes infinitely worse, obviously. The pain crescendos
    to an overwhelming roar. In the midst of the blinding, pulsing,
    volcanic pain, you start to hallucinate. The image of some kind of
    woodland nymph appears. She’s trying to get your attention.
    It looks very much like she’s yelling at the top of her lungs,
    but over the intensity of the pain you can barely hear her words:
    “Hey you! Did you know? Creativity can SAVE YOUR LIFE!"
    """)

def bed():
    print("""
    You drift into a vivid dream. You are hanging by your sweaty palms
    from a tree branch over a large expanse of water. You try to swing
    your legs up over the branch but you’re too weak. You’re starting
    to lose your grip. Suddenly a fairy appears right in front of your face.
    “Hey you!” she says. “Did you know? Creativity can save your life!"
    """)

def dead(why):
    print(why)
    exit(0)

start()
