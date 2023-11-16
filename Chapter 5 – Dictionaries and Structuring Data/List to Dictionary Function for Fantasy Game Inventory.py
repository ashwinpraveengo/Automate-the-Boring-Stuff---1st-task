inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin','dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for j in addedItems:
        if j in inventory:
            inventory[j]=inventory[j]+1
        else:
            inventory.setdefault(j,0)
            inventory[j]=inventory[j]+addedItems.count(j)
    return inventory

def displayInventory(inventory):
    item_total=0
    for k, v in inventory.items():
        print(v,k)
        item_total+=v
    print("Total number of items: " + str(item_total))

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)