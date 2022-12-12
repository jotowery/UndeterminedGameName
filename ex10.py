tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \ a \ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print('''
I\'m trying triple single quotes now
''')

print('Now I\'m going to do a vertical tab. Watch me...\vSo what exactly just happened?')

print("If it's shorter, \vwhat is the vertical tab then")

# this is Unicode and doesn't work with my system
# print("what the hell is 16 bit hex value \uxxxx ummmm")

# Didn't work
# Does ASCII bell do anything\bFor me

# It returned "returntry carriage" --?
print("let's try carriage\rreturn")

# It returned "carriage returng" --?
print("""
I am again trying \r carriage return""")
