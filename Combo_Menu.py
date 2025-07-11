#here I define a variable and create a list that will update as the program gets input.
total_cost = 0.0
items_ordered = []

print("Welcome to the Combo Menu!\n")

#code for the sandwich selection
attempts = 0
while attempts < 3:
    sandwich = input(f"Enter sandwich choice (chicken/beef/tofu) [Attempt {attempts + 1} of 3]: ")
    if sandwich == "chicken":
        total_cost += 5.25
        items_ordered.append("Chicken sandwich")
        break
    elif sandwich == "beef":
        total_cost += 6.25
        items_ordered.append("Beef sandwich")
        break
    elif sandwich == "tofu":
        total_cost += 5.75
        items_ordered.append("Tofu sandwich")
        break
    else:
        print("Please enter a valid sandwich choice.")
        attempts += 1

#code for the drink selection and the while loops make it so that if the user doesn't provide a valid input, it will ask the question again
attempts = 0
while attempts < 3:
    drink_choice = input(f"Do you want a drink? (yes/no) [Attempt {attempts + 1} of 3]: ")
    if drink_choice == "yes":
        drink_size_attempts = 0
        while drink_size_attempts < 3:
            print("Drink Sizes:\n1. Small ($1.00)\n2. Medium ($1.75)\n3. Large ($2.25)")
            drink_size = input(f"Enter drink size (small/medium/large) [Attempt {drink_size_attempts + 1} of 3]: ")
            if drink_size == "small":
                total_cost += 1.00
                items_ordered.append("Small drink")
                break
            elif drink_size == "medium":
                total_cost += 1.75
                items_ordered.append("Medium drink")
                break
            elif drink_size == "large":
                total_cost += 2.25
                items_ordered.append("Large drink")
                break
            else:
                print("Please enter a valid drink size.")
                drink_size_attempts += 1
        break
    elif drink_choice == "no":
        break
    else:
        print("Please enter 'yes' or 'no'.")
        attempts += 1

#code for the fries selection
#the while loops make it so that if the user doesn't provide a valid input, it will ask the question again
attempts = 0
while attempts < 3:
    fries_choice = input(f"Do you want fries? (yes/no) [Attempt {attempts + 1} of 3]: ")
    if fries_choice == "yes":
        size_attempts = 0
        while size_attempts < 3:
            print("Fries Sizes:\n1. Small ($1.00)\n2. Medium ($1.50)\n3. Large ($2.00)")
            fries_size = input(f"Enter fries size (small/medium/large) [Attempt {size_attempts + 1} of 3]: ")
            if fries_size == "small":
                mega_attempts = 0
                while mega_attempts < 3:
                    mega_size = input(f"Do you want to mega-size your fries? (yes/no) [Attempt {mega_attempts + 1} of 3]: ")
                    if mega_size == "yes":
                        total_cost += 2.00
                        items_ordered.append("Large fries (mega-sized)")
                        break
                    elif mega_size == "no":
                        total_cost += 1.00
                        items_ordered.append("Small fries")
                        break
                    else:
                        print("Please enter 'yes' or 'no'.")
                        mega_attempts += 1
                break
            elif fries_size == "medium":
                total_cost += 1.50
                items_ordered.append("Medium fries")
                break
            elif fries_size == "large":
                total_cost += 2.00
                items_ordered.append("Large fries")
                break
            else:
                print("Please enter a valid fries size.")
                size_attempts += 1
        break
    elif fries_choice == "no":
        break
    else:
        print("Please enter 'yes' or 'no'.")
        attempts += 1

#code for the ketchup selection and the 'try' part tries the code and if it doesn't work, then it goes to the except part
attempts = 0
while attempts < 3:
    try:
        ketchup_packets = int(input(f"How many ketchup packets would you like? ($0.25 each) [Attempt {attempts + 1}/3]: "))
        if ketchup_packets >= 0:
            total_cost += 0.25 * ketchup_packets
            if ketchup_packets > 0:
                items_ordered.append(f"{ketchup_packets} Ketchup packets")
            break
        else:
            print("Please enter a non-negative number.")
            attempts += 1
    except:
        print("Please enter a whole number.")
        attempts += 1

#combo discount code
if sandwich in ["chicken", "beef", "tofu"] and drink_choice == "yes" and fries_choice == "yes":
    total_cost -= 1.00
    discount = True
else:
    discount = False

#order summary code
print("\nOrder Summary")
for item in items_ordered:
    print("-", item)
if discount:
    print("Combo discount applied: -$1.00")
print("Total cost: $", total_cost)
