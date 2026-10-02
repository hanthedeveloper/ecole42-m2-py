import random

print("=== Game Data Alchemist ===")

players = ['Alice', 'bob', 'Charlie', 'dylan',
           'Emma', 'Gregory', 'john', 'kevin', 'Liam']
print("Initial list of players:", players)

cap = [i.capitalize() for i in players]
print("New list with all names capitalized:", cap)

only_cap = [i for i in players if i[0].isupper()]
print("New list of capitalized names only:", only_cap)

mydict = {name: random.randint(0, 1000) for name in cap}
print("Score dict:", mydict)

avg = sum([mydict[name] for name in mydict]) / len(mydict)
print("Score average is", round(avg, 2))

newdict = {n: mydict[n] for n in mydict if mydict[n] > avg}
print("High scores:", newdict)
