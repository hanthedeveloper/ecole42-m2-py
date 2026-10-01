import random
import typing

players = ['charlie', 'bob', 'dylan', 'alice']
actions = ['run', 'eat', 'sleep', 'grab', 'move', 'climb', 'swim', 'release', 'use']

def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(players), random.choice(actions))
print("=== Game Data Stream Processor ===")
for i in range(1000):
    gen = next(gen_event())
    player, action = gen
    print(f"Event {i}: Player {player} did action {action}")