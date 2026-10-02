def input_temperature(temp_str: str) -> int:
    degree = int(temp_str)
    if degree > 40:
        raise ValueError(f"{degree}°C is too hot for plants (max 40°C)")
    if degree < 0:
        raise ValueError(f"{degree}°C is too cold for plants (min 0°C)")
    return degree


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()

    test_values = ["25", "abc", "100", "-50"]

    for value in test_values:
        print(f"Input data is '{value}'")
        try:
            temp = input_temperature(value)
            print(f"Temperature is now {temp}°C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
