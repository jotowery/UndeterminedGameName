f = open("capnnemo.txt", "a")
f.truncate()
f.close()

f = open("capnnemo.txt", "r")
print(f.read())

f = open("capnnemo.txt", "w")
f.write("I never said anything about Nemo. \n You wanna know more? Ask me.")
f.close()

f = open("capnnemo.txt", "a")
f.write("This is how you write. You say f.write, put a (, and then you write.")
f.close()

f = open('capnnemo.txt', 'r')
print(f.read())
