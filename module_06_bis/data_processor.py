import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self.wdata: list[str] = []
        self.counter: int = -1

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        try:
            popdata = self.wdata.pop(0)
        except IndexError:
            raise ValueError("no data to pop.")
        else:
            self.counter += 1
        return (self.counter, popdata)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(i, (int, float)) for i in data)
        else:
            return isinstance(data, (float, int))

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            self.wdata.extend(str(i) for i in data)
        else:
            self.wdata.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(i, str) for i in data)
        else:
            return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            self.wdata.extend(i for i in data)
        else:
            self.wdata.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            return all(check_helper(i) for i in data)
        else:
            return check_helper(data)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper data")
        newlist = []
        try:
            if isinstance(data, dict):
                data = [data]
            for i in data:
                newlist.append(i['log_level'] + ": " + i['log_message'])
        except KeyError as e:
            raise ValueError(e)
        self.wdata.extend(newlist)


def check_helper(my_dict: dict[str, str]) -> bool:
    if isinstance(my_dict, dict):
        return (all(isinstance(i, str) for i in my_dict.keys())
                and all(isinstance(i, str) for i in my_dict.values())
                and "log_level" in my_dict
                and "log_message" in my_dict)
    else:
        return False


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    num = NumericProcessor()
    print(f" Trying to validate input '42': {num.validate(42)}")
    print(f" Trying to validate input 'Hello': {num.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior "
          "validation:")
    try:
        num.ingest("foo")
    except ValueError as e:
        print(f" Got exception: {e}")
    numbers: list[int | float] = [1, 2, 3, 4, 5]
    print(f" Processing data: {numbers}")
    num.ingest(numbers)
    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = num.output()
        print(f" Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    text = TextProcessor()
    print(f" Trying to validate input '42': {text.validate(42)}")
    words = ["Hello", "Nexus", "World"]
    print(f" Processing data: {words}")
    text.ingest(words)
    print(" Extracting 1 value...")
    for _ in range(1):
        rank, value = text.output()
        print(f" Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    log = LogProcessor()
    print(f" Trying to validate input 'Hello': {log.validate('Hello')}")
    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f" Processing data: {logs}")
    log.ingest(logs)
    print(" Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f" Log entry {rank}: {value}")