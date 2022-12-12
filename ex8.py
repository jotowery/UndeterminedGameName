# formatter is a variable standing in for a string of 4 undefined strings separated by spaces
# QUESTION: Is formatter a string or a variable? He refers to both on p60
# *** We tell python, Here is a string called format
formatter = "{} {} {} {}"

# .format tells python that the four things separated by commas are going in the places left for strings {} in the format definition. Print tells python to print what formatter is with the numbers here filling in the {} in the formatter definition
# *** We tell python to run a command named format (format function) on the formatter string. We pass four arguments to the format function, which match up with the four {} in the formatter variable.
print(formatter.format(1, 2, 3, 4, 5, 6, 7)) # --> Interesting that adding 5, 6, 7 did not break the program. Nothing changed when I executed it.
print("one", "two", "three", "four")
# Instead of numbers, we gave Python Boolean values for the 4 strings.

print(formatter.format(True, False, False, True))

# now we are just printing whatever is in " " in the formatter definition. 
# QUESTION: I'm not sure why it prints those characters if they usually aren't printed and indicate a different operation. 

print(formatter.format(formatter, formatter, formatter, formatter))

# Now we tell python to put some other strings in the places for strings in the format definition.
print(formatter.format(
    "I'm always writing",
    "songs that you could",
    "sing with me if you",
    "WANT TO!"
))

#Looks like commas separate strings with a space rather than hard return even if code is written on different lines
