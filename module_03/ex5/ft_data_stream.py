import random
import typing


players = ['charlie', 'bob', 'dylan', 'alice']
actions = ['run', 'eat', 'sleep', 'grab', 'move', 'climb',
           'swim', 'release', 'use']


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(players), random.choice(actions))


print("=== Game Data Stream Processor ===")
obj = gen_event()
for i in range(1000):
    player, action = next(obj)
    print(f"Event {i}: Player {player} did action {action}")


newlist: list[tuple[str, str]] = []
i = 0
obj = gen_event()
while i < 10:
    newlist = newlist + [next(obj)]
    i += 1
print("Built list of 10 events:", newlist)


def consume_event(
                    mylist: list[tuple[str, str]]
                 ) -> typing.Generator[tuple[str, str], None, None]:
    while len(mylist) > 0:
        event = random.choice(mylist)
        j = 0
        while mylist[j] != event:
            j += 1
        mylist[:] = mylist[:j] + mylist[j + 1:]
        yield event


for event in consume_event(newlist):
    print("Got event from list:", event)
    print("Remains in list:", newlist)
