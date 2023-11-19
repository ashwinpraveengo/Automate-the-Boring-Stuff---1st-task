import pyinputplus as pyip

bo={'wheat': 2, 'white': 2, 'sourdough': 2.5}
po={'chicken': 3, 'turkey': 3.5, 'ham': 3.0, 'tofu': 4.0}
co={'cheddar': 1, 'Swiss': 1.5, 'mozzarella': 1.5}
condo={'mayo': 0.5, 'mustard': 0.5, 'lettuce': 0.5, 'tomato': 0.5}

bt=pyip.inputMenu(["wheat","white","sourdough"],prompt="Enter bread type: ") 
pt=pyip.inputMenu(['chicken','turkey','ham','tofu'],prompt="Enter protein type: ")
yn=pyip.inputYesNo("Do you want cheese: ")
yn=yn.upper()

if yn == "YES":
    ct=pyip.inputMenu(["cheddar","Swiss","mozzarella"],prompt="Enter cheese type: ")
else:
    ct = None

m=pyip.inputYesNo("Do you want mayo, mustard, lettuce, or tomato: ")
n=pyip.inputInt("How many sandwiches do you want? :", min=1)  

total_cost = n * (bo[bt] + po[pt] + (co[ct] if ct else 0))
print("Total cost will be:", total_cost)
