def Mad_Libs_1(a, b, c, d, e):
    print(f"I had a {a} in my pocket when I met you.")
    print(f"I had a book called _{b}_ on my coffee table that one time you called me.")
    print(f"If you ever decide to {c}, I guess I'll have to go bungee jumping.")
    print(f"When I jump, you'll hear me holler, '{d}!!!'")
    print(f"It's a good thing we're such good {e}.")

print("\n")

noun = input("Give me a noun. Please.  ")
proper_noun = input("Great. Now I need a Proper Noun.   ")
verb = input("Very well. Now hit me with your best verb.   ")
silly_word = input("Please give me a very silly Silly Word.   ")
plural_noun = input("This is your final opportunity to give me a word. For this last entry, I need a plural noun.   ")

print("\n")
print("Thank you for your participation in this Mad Libs Experience. You may now read your amazing story.   ")
print("\n")

Mad_Libs_1(noun, proper_noun, verb, silly_word, plural_noun)


Mad_Libs_1
