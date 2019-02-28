'''
Created on Feb 26, 2019

@author: alan3
Imagine that a vanquished dragons loot is represented as a list of strings like this:
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Write a function named addToInventory(inventory, addedItems), where the inventory
 parameter is a dictionary representing the player's inventory (like in the previous project) 
 and the addedItems parameter is a list like dragonLoot. The addToInventory() function should 
 return a dictionary that represents the updated inventory. Note that the addedItems list can 
 contain multiples of the same item. Your code could look something like this:


def addToInventory(inventory, addedItems):
    # your code goes here

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
The previous program (with your displayInventory() function from the previous project) would output the following:


Inventory:
45 gold coin
1 rope
1 ruby
1 dagger

Total number of items: 48

'''

def addToInventory(inventory, addedItems):
    for thing in addedItems:
        inventory.setdefault(thing, 0)
        inventory[thing] = inventory[thing] + 1
    return inventory

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + str(k) )
        item_total = item_total + v
    print("Total number of items: " + str(item_total))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

