x = format(23, '+')

print(x)



f = open("capnnemo.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

f = open("capnnemo.txt", "a")
f.truncate(20)
f.close()

f = open("capnnemo.txt", "r")
print(f.read())
