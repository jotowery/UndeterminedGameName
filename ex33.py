

def myfrootyfunction(McMan, McScroogiepuss):
    i = 0
    numbers = []
    while i < McMan:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + McScroogiepuss

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")
    for num in numbers:
        print(num)

myfrootyfunction(80, 10)
