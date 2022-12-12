
print("I am reviewing variables.")

print("My first variable is called silly_words.")

silly_word = 'xxxxxxx'

print("I have a silly word:", silly_word)

my_name = 'Jo Verdis'
my_age = 41
my_height = 64
my_weight = 123 * 0.45
my_eyes = 'green'
my_teeth = 'yellow'
my_hair = 'brown'

print(f"Let's talk about {my_name}.")
print(f"She's {my_height} inches tall.")
print(f"She's {my_weight} kilos heavy.")
print(f"She's got {my_eyes} eyes and {my_hair} hair.")
print(f"Her teeth are {my_teeth} but she's working on that.")

print('**************')
types_of_people = 10
#so he set a variable to a value that is actually a formatted string with another variable insdie it
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

print("*********")

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "I'm trying",
    "to make a little text",
    "here, because",
    "I was invited to do that."
))

print("******")
print("I am 6'2\" tall.")

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

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
