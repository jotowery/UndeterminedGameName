i = 0
numbers = []

def myloopythang(big_number, increment):

    i = 0
    numbers = []
    while i < big_number:
        print(f"At the top i  is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


        print("The numbers: ")

        for num in numbers:
            print(num)

print(myloopythang(12, 2))
