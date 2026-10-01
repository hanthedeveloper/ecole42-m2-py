import random

ACHIEVEMENTS = [
                'Crafting Genius', 'World Savior', 'Master Explorer',
                'Collector Supreme', 'Untouchable', 'Boss Slayer',
                'Strategist', 'Unstoppable', 'Speed Runner', 'Survivor',
                'Treasure Hunter', 'First Steps', 'Sharp Mind',
                'Hidden Path Finder'
                ]

def gen_player_achievements() -> set[str]:
    t = random.randint(5, 9)
    return (set(random.sample(ACHIEVEMENTS, t)))

print("=== Achievement Tracker System ===")
print()
alice = gen_player_achievements()
bob = gen_player_achievements()
charlie = gen_player_achievements()
dylan = gen_player_achievements()
print("Player Alice:", alice)
print("Player Bob:", bob)
print("Player Charlie:", charlie)
print("Player Dylan:", dylan)
print()
print("All distinct achievements:", set.union(alice, bob, charlie, dylan))
print()
print("Common achievements:", set.intersection(alice, bob, charlie, dylan))
print()
print("Only Alice has:", set.difference(alice, set.union(bob, charlie, dylan)))
print("Only Bob has:", set.difference(bob, set.union(alice, charlie, dylan)))
print("Only Charlie has:", set.difference(charlie, set.union(alice, bob, dylan)))
print("Only Dylan has:", set.difference(dylan, set.union(alice, bob, charlie)))
print()
print("Alice is missing:", set.difference(set(ACHIEVEMENTS), alice))
print("Bob is missing:", set.difference(set(ACHIEVEMENTS), bob))
print("Charlie is missing:", set.difference(set(ACHIEVEMENTS), charlie))
print("Dylan is missing:", set.difference(set(ACHIEVEMENTS), dylan))