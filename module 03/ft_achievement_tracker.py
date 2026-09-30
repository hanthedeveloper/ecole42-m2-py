import random

ACHIEVEMENTS = [
                'Taking Inventory', 'Getting Wood', 'Benchmaking',
                'Time to Mine!', 'Monster Hunter', 'Acquire Hardware',
                'DIAMONDS!', 'Adventuring Time', 'Into The Nether', 'The Lie',
                'Local Brewery', 'Iron Belly', 'Enchanter', 'Overpowered',
                'Time to Farm!', 'Cheating Death', 'Zombie Doctor', 'Body Guard',
                'The End?', 'Whatever Floats Your Goat'
                ]

def gen_player_achievements() -> set[str]:
    t = random.randint(7, 15)
    return (set(random.sample(ACHIEVEMENTS, t)))

print("=== Achievement Tracker System ===")
print()
steve = gen_player_achievements()
alex = gen_player_achievements()
noor = gen_player_achievements()
kai = gen_player_achievements()
print("player steve:", steve)
print("player alex:", alex)
print("player noor:", noor)
print("player kai:", kai)
print()
print("all distinct achievements:", set.union(steve, alex, noor, kai))
print()
print("common achievements:", set.intersection(steve, alex, noor, kai))
print()
print("only steve has:", set.difference(steve, set.union(alex, noor, kai)))
print("only alex has:", set.difference(alex, set.union(steve, noor, kai)))
print("only noor has:", set.difference(noor, set.union(alex, steve, kai)))
print("only kai has:", set.difference(kai, set.union(alex, noor, steve)))
print()
print("steve is missing:", set.difference(set(ACHIEVEMENTS), steve))
print("alex is missing:", set.difference(set(ACHIEVEMENTS), alex))
print("noor is missing:", set.difference(set(ACHIEVEMENTS), noor))
print("kai is missing:", set.difference(set(ACHIEVEMENTS), kai))
