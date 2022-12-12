
# types_of_people is a variable.
# QUESTION: is types_of_people a string?
# QUESTION: I'm not sure of answer on Study Drill 2 on page 53
types_of_people = 10

# = this is an f-string (format) using a variable in {} inside a string
x = f"There are {types_of_people} types of people."

# more variables
binary = "binary"
do_not = "don't"

# Another formatted string including variables
y = f"Those who know {binary} and those who {do_not}."

# printing variables
print(x)
print(y)

# printing formatted strings with variables
print(f"I said: {x}")
print(f"I also said: '{y}'")

# variables
hilarious = False

# QUESTION: Why are there {} inside the quotes?
joke_evaluation = "Isn't that joke so funny?! {}"

# QUESTION - what is the "." for?
print(joke_evaluation.format(hilarious))

# variables
w = "This is the left side of..."
e = "a string with a right side."

# addition with variables
print (w + e)


