def ft_plant_age() -> None:
    day = int(input("Enter plant age in days: "))
    if (day > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
