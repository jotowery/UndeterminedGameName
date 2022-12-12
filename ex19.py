# defining a function with two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # writing the code for what will be printed when values are associated with the arguments in the function
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
# assigning numeric values to the arguments in the function using parentheses
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
# assigning numeric values to the arguments using = like normal variables
amount_of_cheese = 10
amount_of_crackers = 50

# assigning numeric values to the arguments using math inside ()
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# using variables, which have already been given values, in combination with math, inside () to define the arguments
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
