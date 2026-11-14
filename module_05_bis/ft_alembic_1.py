import alchemy


if __name__ == "__main__":
    print("=== Alembic 1 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    test_air = alchemy.create_air()
    print("Testing create_air:", test_air)
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print("Testing the hidden create_earth: ", end="")
    print(alchemy.create_earth())
