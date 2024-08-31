print("Welcome to the tip calculator!")
totalCost = round(float((input("What was the total bill?"))), 2)
tipPerc = int((input("How much would you like to tip?\n0, 10, 12, or 15?")))
split = int((input("How many people are splitting the bill?")))
totalTip = round(totalCost / tipPerc, 2)
totalCostSplit = round(totalCost / split, 2)
totalTipSplit = round(totalTip / split, 2)
totalTipCostSplit = round(totalCostSplit + totalTipSplit, 2) 

print(f"The total cost will be ${totalCost} and" + f"The total tip will be ${(totalTip)}")
print(f"Split amoung {split} people \neach person will pay ${totalCostSplit} \neach person will tip ${totalTipSplit}\
      \ntogether that is ${totalTipCostSplit} per person")

