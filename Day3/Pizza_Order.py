print("Welcome to Python Pizza Deliveries!!!")
size = input("What size pizza do you want? S, M, L. ")
add_pepperoni = input("Do you want pepperoni? Y or N. ")
extra_cheese = input("Do you want extra cheese? Y or N. ")
money = 0

if size == "S":
    money += 15
elif size == "M":
    money += 20
else:
    money += 25

if add_pepperoni == "Y":
    if size == "S":
        money += 2
    else:
        money += 3

if extra_cheese == "Y":
    money += 1

print(f"Your final money is {money}")