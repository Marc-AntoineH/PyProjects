def displayInventory(items):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print('  ' + str(v) + ' ' + str(k))
        item_total += v
    print("Total number of items: " + str(item_total))

inventory = {'arrow': 12,
             'gold coin': 42,
             'rope': 1,
             'torch': 6,
             'dagger': 1}

displayInventory(inventory)
