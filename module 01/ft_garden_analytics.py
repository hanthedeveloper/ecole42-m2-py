class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)
        self._stats = self.StatsClass()

    def get_stats(self) -> "Plant.StatsClass":
        return self._stats

    @staticmethod
    def check(age: int) -> int:
        return age > 365

    @classmethod
    def create(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    class StatsClass:
        def __init__(self) -> None:
            self._age_count = 0
            self._grow_count = 0
            self._show_count = 0

        def add_grow(self) -> None:
            self._grow_count += 1

        def add_age(self) -> None:
            self._age_count += 1

        def add_show(self) -> None:
            self._show_count += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow,", end=" ")
            print(f"{self._age_count} age,", end=" ")
            print(f"{self._show_count} show")

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

    def grow(self, rate: float = 1.0) -> None:
        self._stats.add_grow()
        self.set_height(round(self.get_height() + rate, 2))

    def age(self, days: int = 1) -> None:
        self._stats.add_age()
        self.set_age(self.get_age() + days)

    def show(self) -> None:
        self._stats.add_show()
        print(f"{self.name}: {self.get_height()}cm, {self.get_age()} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    def bloom(self) -> None:
        self._bloomed = True


class Seed(Flower):
    def __init__(
                self,
                name: str,
                height: float,
                age: int,
                color: str
                ) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


class Tree(Plant):
    def __init__(
                self,
                name: str,
                height: float,
                age: int,
                trunk_diameter: float
                ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._stats: Tree.StatsClass = Tree.StatsClass()

    class StatsClass(Plant.StatsClass):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def add_shade(self) -> None:
            self._shade_count += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_count} shade")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self._stats.add_shade()
        print(f"Tree {self.name} now produces a shade of", end=" ")
        print(f"{self.get_height()}cm long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0.0

    def grow(self, rate: float = 1.0) -> None:
        super().grow(rate)
        self.nutritional_value += 0.5

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def show_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.get_stats().display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("\n=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    show_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    show_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    show_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    show_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    show_statistics(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.create()
    unknown.show()
    show_statistics(unknown)
