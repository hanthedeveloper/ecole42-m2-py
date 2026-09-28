def ft_water_reminder() -> None:
    day = int(input("Days since last watering: "))
    if (day > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
