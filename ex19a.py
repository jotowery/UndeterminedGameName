def book_sales(family, friends, strangers):
    print(f"I got {family} sales from family members!")
    print(f"I got {friends} sales from friends!")
    print(f"I got {strangers} sales from strangers!")
    print(f"That's {family + friends + strangers} total sales!")

book_sales(20, 50, 535747)

print("This time, I got more sales:")
family = 22
friends = 55
strangers = 635747

book_sales(family, friends, strangers)

print("EVEN MORE SALES!!!!!")
book_sales(family + 100, friends + 200, strangers + 10000)
