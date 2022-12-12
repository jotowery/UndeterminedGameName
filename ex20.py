from sys import argv

script, input_file = argv

# def creates and names a function. print_all is the name of this function
def print_all(f):
    # this is what the function does. f is the argument for print_all. .read is a method that is pre-defined in python
    print(f.read())

# rewind is the name of this function
def rewind(f):
    # .seek is a method in python (method is more or less the same thing as a function)
    # this probably moves the cursor to the first digit which will be 0
    # 0 is an "argument" -- you're telling seek what digit to go to
    f.seek(0)

def print_a_line(line_count, f):
    # line_count and f are arguments = "variables" in a function
    print(line_count, f.readline())

# this is actually a variable (current_file)
# open is another method
current_file = open(input_file)

# this command calls the function current_file
# print_all is a function we defined above. It reads and then prints what is read
# in this case we are reading current_file which is a variable defined above as open(input_file)
# print(open(text.txt).read())
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)


current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 10
print_a_line(current_line, current_file)

# [ current_line = current_line + 1 ] is the same thing as [ current_line += 1 ]
