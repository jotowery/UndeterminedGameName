# this one is like your scripts with argv
# Telling Python to make a function using def for "define"
# On the same line, we give the function a name that says what it does.
# On the same line we tell it we want *args (same as argv but for functions).
# *args has to go in () to work.
# End this line with a :
# All indented (4 spaces) lines following : will become attached to the function name.
# The first indented line unpacks all the arguments
# then we print the arguments
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
# Better than the first way, this way skips unpacking the arguments
# and just uses the names we want inside ().
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
