def ft_chr_helper(i: int, day: int) -> None:
    if i <= day:
        print(f"Day {i}")
        ft_chr_helper(i + 1, day)


def ft_count_harvest_recursive() -> None:
    day = int(input("Days until harvest: "))
    ft_chr_helper(1, day)
    print("Harvest time!")
