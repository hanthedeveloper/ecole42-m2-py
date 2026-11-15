from ex3 import TransformCreatureFactory

if __name__ == "__main__":
    print("Testing Creature with transform capability")
    print(" base:")
    shiftling = TransformCreatureFactory()
    shiftling_base = shiftling.create_base()
    print(shiftling_base.describe())
    print(shiftling_base.attack())
    print(shiftling_base.transform())
    print(shiftling_base.attack())
    print(shiftling_base.revert())
    print(" evolved:")
    shiftling_evolved = shiftling.create_evolved()
    print(shiftling_evolved.describe())
    print(shiftling_evolved.attack())
    print(shiftling_evolved.transform())
    print(shiftling_evolved.attack())
    print(shiftling_evolved.revert())
