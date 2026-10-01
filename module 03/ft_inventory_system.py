import sys

print("=== Inventory System Analysis ===")
inv = {}
i = 1
while i < len(sys.argv):
    ar = sys.argv[i].split(":")
    if len(ar) != 2:
        print(f"Error - invalid parameter '{sys.argv[i]}'")
    elif ar[0] in inv:
        print(f"Redundant item '{ar[0]}' - discarding")
    else:
        try:
            if int(ar[1]) < 0:
                print(f"Error - negative quantity for '{ar[0]}'")
            else:
                inv[ar[0]] = int(ar[1])
        except ValueError as e:
            print(f"Quantity error for '{ar[0]}': {e}")
    i += 1
if len(inv) == 0:
    print("Error - no valid items provided")
else:
    print("Got inventory:", inv)
    print("Item list:", list(dict.keys(inv)))
    total = sum(inv.values())
    print(f"Total quantity of the {len(inv)} items:", total)
    mostab = list(dict.keys(inv))[0]
    leasetab = list(dict.keys(inv))[0]
    if total == 0:
        print("Total quantity is 0, cannot compute percentages")
    else:
        for item in inv:
            percent = round(inv[item] / total * 100, 1)
            print(f"Item {item} represents {percent}%")
    for item in inv:
        if inv[item] > inv[mostab]:
            mostab = item
        if inv[item] < inv[leasetab]:
            leasetab = item
    print(f"Item most abundant: {mostab} with quantity {inv[mostab]}")
    print(f"Item least abundant: {leasetab} with quantity {inv[leasetab]}")
    dict.update(inv, {'magic_item': 1})
    print("Updated inventory:", inv)

