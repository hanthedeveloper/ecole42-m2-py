class Plant:
    name: str
    height: float
    page: int
    rate: float

    def grow(self) -> None:
        self.height += self.rate
        self.height = round(self.height, 2)

    def age(self) -> None:
        self.page += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.page} days old")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    flower = Plant()
    flower.page = 10
    flower.rate = 0.8
    flower.name = "Rose"
    flower.height = 35.4
    first_height = flower.height
    Plant.show(flower)
    for i in range(1, 8):
        Plant.age(flower)
        Plant.grow(flower)
        print(f"=== Day {i} ===")
        Plant.show(flower)
    print(f"Growth this week: {round(flower.height - first_height, 2)}cm")
