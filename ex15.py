# HELP! How to open txt file from within Python? p82 #6????

# argv is a Python module we are using in this instance to get a filename
from sys import argv

# We are telling Python it needs the user to pass (two) command line arguments:
script, filename = argv

# QUESTION: I'm not sure what typing txt tells Python. I guess the use of 'txt' here is linked to below when it says print(txt  ? and then .read tells it to read the text in the .txt file?)
# ANSWERED: txt = open(filename) creates a "file object." Then a confusing analogy about DVD players -- p82

txt = open(filename)

# prints statement, using f-string/function to output the name of the file, which it gets from the user input when we put the filename in at the beginning as a command line argument.
print(f"Here's your file {filename}:")
# prints the contents of the text file
print(txt.read())

# prints instructions to type the filename
print("Type the filename again:")
# > is printed to indicate to user to type the filename here, and input tells Python to assign what the user types after the > to the variable file_again
file_again = input("> ")

# txt_again used as a variable assigned to the command to open the filename the user typed above
txt_again = open(file_again)

# tells Python to print the file by using the command in the last line to open the file, then read it. (Not sure how to put that in English correctly).
# QUESTION: Why is there nothing in the () after read?
print(txt_again.read())

print("What is your last name?")
Last_Name = input("Enter Your Personal Data here:  ")
print(f"{Last_Name} is a pretty sweet surname.")

print("What is your middle name?")
Middle_Name = input("Tell me now:    ")
print(f"{Middle_Name} sounds funny. I don't like it.")

print("What is your first name?")
First_Name = input("I wanna know! ")
print(f"What a beautiful name, {First_Name}. Well done.")

