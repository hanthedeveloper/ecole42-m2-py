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


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(text for i, text in data))


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        items = ", ".join(f'"item_{num}": "{text}"' for num, text in data)
        print("{" + items + "}")


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for input_ in stream:
            for proc in self.processors:
                if proc.validate(input_):
                    proc.ingest(input_)
                    break
            else:
                print(f"DataStream error - Can't process element "
                      f"in stream: {input_}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            name = type(proc).__name__.replace("Processor", " Processor")
            remaining = len(proc.wdata)
            total = proc.counter + 1 + remaining
            print(f"{name}: total {total} items processed, "
                  f"remaining {remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            output_list: list[tuple[int, str]] = []
            for i in range(min(nb, len(self.wdata))):
                output_list.append(self.output())
            plugin.process_output(output_list)

if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...\n")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processors\n")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    input_list1: list[typing.Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [{"log_level": "WARNING",
          "log_message": "Telnet access! Use ssh instead"},
         {"log_level": "INFO",
          "log_message": "User wil is connected"}],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {input_list1}\n")
    stream.process_stream(input_list1)
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVPlugin())
    print()
    stream.print_processors_stats()

    input_list2: list[typing.Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [{"log_level": "ERROR",
          "log_message": "500 server crash"},
         {"log_level": "NOTICE",
          "log_message": "Certificate expires in 10 days"}],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"\nSend another batch of data: {input_list2}\n")
    stream.process_stream(input_list2)
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONPlugin())
    print()
    stream.print_processors_stats()