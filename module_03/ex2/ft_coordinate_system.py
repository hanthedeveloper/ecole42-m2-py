import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = raw.split(",")
        try:
            a, b, c = parts
        except ValueError:
            print("Invalid syntax")
            continue
        try:
            for i in parts:
                float(i)
            return (float(a), float(b), float(c))
        except ValueError as e:
            print(f"Error on parameter '{i}': {e}")


try:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    one = get_player_pos()
    print("Got a first tuple:", one)
    xo, yo, zo = one
    print(f"It includes: X={xo}, Y={yo}, Z={zo}")
    try:
        res1 = math.sqrt(xo**2 + yo**2 + zo**2)
        print(f"Distance to center: {round(res1, 4)}")
    except OverflowError:
        print("Distance too large to compute")
    print()
    print("Get a second set of coordinates")
    two = get_player_pos()
    xn, yn, zn = two
    try:
        res2 = math.sqrt((xn - xo)**2 + (yn - yo)**2 + (zn - zo)**2)
        print(f"Distance between the 2 sets of coordinates: {round(res2, 4)}")
    except OverflowError:
        print("Distance too large to compute")
except (EOFError, KeyboardInterrupt):
    print("\nInput interrupted.")
