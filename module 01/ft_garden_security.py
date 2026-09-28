class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def grow(self, rate: float) -> None:
        self._height += rate
        self._height = round(self._height, 2)

    def age(self) -> None:
        self._age += 1

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self.name}: {self.get_height()}cm, {self.get_age()} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()

    new_height = 0.0
    new_age = 0
    rose.set_height(new_height)
    print(f"Height updated: {new_height}cm")
    rose.set_age(new_age)
    print(f"Age updated: {new_age} days\n")

    rose.set_height(-5)
    rose.set_age(-3)

    print("\nCurrent state: ", end="")
    rose.show()
