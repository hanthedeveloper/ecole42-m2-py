from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4 import (
    AggressiveStrategy,
    InvalidStrategy,
    BattleStrategy,
    NormalStrategy,
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    names = ", ".join(
        f"({fac.create_base().name}+"
        f"{type(strat).__name__.replace('Strategy', '')})"
        for fac, strat in opponents
    )
    print(f" [ {names} ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    try:
        for outside in range(len(opponents)):
            for inside in range(outside + 1, len(opponents)):
                fac_1, strtgy_1 = opponents[outside]
                fac_2, strtgy_2 = opponents[inside]
                creature_1 = fac_1.create_base()
                creature_2 = fac_2.create_base()
                print("\n* Battle *")
                print(creature_1.describe())
                print(" vs.")
                print(creature_2.describe())
                print(" now fight!")
                strtgy_1.act(creature_1)
                strtgy_2.act(creature_2)
    except InvalidStrategy as e:
        print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    flame = FlameFactory()
    transform = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()

    print("Tournament 0 (basic)")
    battle([(flame, normal), (transform, aggressive)])

    print("\nTournament 1 (error)")
    battle([(transform, aggressive), (flame, aggressive)])
