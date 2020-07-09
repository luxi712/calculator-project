#1. Sum up the value of the order
#Ask what the budget is
print("Welcome to Shake Shack!")
budget_prompt = "What is your budget? "
budget = int(input(budget_prompt))

total = []

burger_choice = "What burger would you like? "
burger = input(burger_choice)
if burger.lower() == "shackburger" or "cheeseburger":
    total.append(5.99)
elif burger.lower() == "smokeshack":
    total.append(7.49)
elif burger.lower() == "veggieshack" or "chickenshack":
    total.append(7.29)
elif burger.lower() == "shroomburger":
    total.append(7.69)
elif burger.lower() == "hamburger":
    total.append(5.39)
elif burger.lower() == "shacksack":
    total.append(10.89)

side_choice = "Which fries would you like? "
side = input(side_choice)
if side.lower() == "crinkle cut fries":
    total.append(3.09)
elif side.lower() == "cheese fries":
    total.append(4.09)
elif side.lower() == "bacon cheese fries":
    total.append(5.09)
else:
    total.append(0)

shake_choice = "What shake would you like? "
shake = input(shake_choice)
if shake.lower() == "vanilla" or "strawberry" or "chocolate" or "salted caramel" or "cookies and creme":
    total.append(5.49)
elif shake.lower() == "smoresshake":
    total.append(5.99)
else: 
    total.append(0)

#2. check whether or not it meets the budget constraints
if sum(total) > budget:
    print("You're over your budget by: $" + str(sum(total) - budget) + ".")
elif sum(total) == budget:
    print("You have: $0 remaning.")
else:
    print("You have $" + str(budget - sum(total)) + " remaining.")

print("Your subtotal is: $" + str(sum(total)))

#3. Add tip
asktip = "Would you like to add a tip? "
tipyesno = input(asktip)

if tipyesno.lower() == "yes":
    tippercent = "What percentage of your total would you like to tip? "
    tipdecimal = input(tippercent)
    tip = (int(tipdecimal)/100)*sum(total)
    print("You will be tipping $" + str(round(tip, 2)) + ".")
    print("Your total will be $" + (str(round(tip, 2) + sum(total))) + ".")
else:
    print("Your total will be: $" + str(sum(total)))