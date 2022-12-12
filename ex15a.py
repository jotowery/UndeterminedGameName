# QUESTION: p82, #5. Why is one way of getting a file name better than the other? (argv vs. input) I don't know???

# Ask for input
print("What file do you request?")

# Assign user input to variable called filename, give user a > prompt before their input
filename = input("> ")
# print, referencing the filename given by the user as a function
print(f"As you requested, I present to you, the Great File {filename}")

# assign the command to open the file to the variable, TheGreatFile
TheGreatFile =open(filename)

# Q: Did I get this right?: the variable TheGreatFile is assigned to the command to open a file (above). This next thing tells Python to read the file after opening it, and print the contents of the file, all in one command.
print(TheGreatFile.read())

print("Tell me what you want to know.")
want2know = input("> ")
print(f"I have the answers you seek. They are contained within The Great Text, {filename}.")
txt = open(filename)
print(txt.read())
