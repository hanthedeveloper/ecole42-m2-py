class GardenError(Exception):
    def __init__(
                self,
                mesg: str = "Unknown garden error"
                ) -> None:
        Exception.__init__(self, mesg)


class PlantError(GardenError):
    def __init__(
                self,
                mesg: str = "Unknown plant error"
                ) -> None:
        GardenError.__init__(self, mesg)


class WaterError(GardenError):
    def __init__(
                self,
                mesg: str = "Unknown water error"
                ) -> None:
        GardenError.__init__(self, mesg)


def plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing WaterError...")
    try:
        water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
