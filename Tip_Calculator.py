print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? € "))
perc = float(input("What percentage tip would you like to give? 5, 10, 12 or 15? € "))
peop = int(input("How many people to split the bill? "))
bill_w_tip = (bill / 100 * perc) + bill
total = bill_w_tip / peop
amount = (round(total, 2))
amount = "{:.2f}".format(total)
print(f"Each person should pay € {amount}.")