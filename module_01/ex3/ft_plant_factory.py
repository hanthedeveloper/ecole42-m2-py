class Plant:
    def __init__(self, name: str, height: float, page: int) -> None:
        self.name = name
        self.height = height
        self.page = page

    def grow(self, rate: float) -> None:
        self.height += rate
        self.height = round(self.height, 2)

    def age(self) -> None:
        self.page += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.page} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunf = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)
    print("=== Plant Factory Output ===")
    print("Created: ", end="")
    rose.show()
    print("Created: ", end="")
    oak.show()
    print("Created: ", end="")
    cactus.show()
    print("Created: ", end="")
    sunf.show()
    print("Created: ", end="")
    fern.show()
