from ex3 import CreatureFactory, FlameFactory
from ex3 import TransformCreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def battle(first: CreatureFactory, second: CreatureFactory) -> None:
    first_base = first.create_base()
    second_base = second.create_base()

    print(first_base.describe())
    print(" vs.")
    print(second_base.describe())
    print(" fight!")
    print(first_base.attack())
    print(second_base.attack())


if __name__ == "__main__":
    print("Testing factory")
    flame = FlameFactory()
    test_factory(flame)

    print()
    print("Testing factory")
    trans = TransformCreatureFactory()
    test_factory(trans)

    print()
    print("Testing battle")
    battle(flame, trans)
