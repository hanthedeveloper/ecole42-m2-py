import sys

print("=== Inventory System Analysis ===")
inv: dict[str, int] = {}
i = 1
while i < len(sys.argv):
    arg = sys.argv[i]
    parts = arg.split(":")
    if len(parts) != 2 or parts[0].strip() == "":
        print(f"Error - invalid parameter '{arg}'")
    elif parts[0] in inv:
        print(f"Redundant item '{parts[0]}' - discarding")
    else:
        try:
            quantity = int(parts[1])
            if quantity < 0:
                print(f"Error - negative quantity for '{parts[0]}'")
            else:
                inv[parts[0]] = quantity
        except ValueError as e:
            print(f"Quantity error for '{parts[0]}': {e}")
    i += 1

print("Got inventory:", inv)
items = list(inv.keys())
print("Item list:", items)
total = sum(inv.values())
print(f"Total quantity of the {len(inv)} items:", total)
if total == 0:
    print("Total quantity is 0, cannot compute percentages")
else:
    for item in inv:
        percent = round(inv[item] / total * 100, 1)
        print(f"Item {item} represents {percent}%")
if len(inv) > 0:
    most = items[0]
    least = items[0]
    for item in inv:
        if inv[item] > inv[most]:
            most = item
        if inv[item] < inv[least]:
            least = item
    print(f"Item most abundant: {most} with quantity {inv[most]}")
    print(f"Item least abundant: {least} with quantity {inv[least]}")
inv.update({'magic_item': 1})
print("Updated inventory:", inv)
