
# prints string
print("Mary had a little lamb.")
# string inside string using f-string (format).
# QUESTION: Why use .format('snow')? just for string inside a string demonstration purposes?
print("Its fleece was white as {}.".format('whatever'))
# prints string
print("And everywhere that Mary went.")
# prints . or whatever's in "" string the number of times indicated by the number following *
print("." * 10) #what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens

# since end1, end2 etc are variables and not numbers, end1 + end2 etc just prints them next to each other
# end=' ' printed a space instead of a return to the next line. What I don't get is why the word end gave that command. We didn't have end set up as a variable. Is that a specific command in Python?
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)