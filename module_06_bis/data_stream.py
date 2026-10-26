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
                print("gecersız ınput")


if __name__ == "__main__":
    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    data = DataStream()
    data.register_processor(num)
    data.register_processor(text)
    data.register_processor(log)

    var = 5
    liste = [None, "42", 42, "hello", var, {"log_level": "ERROR", "log_message": "something failed"}]

    data.process_stream(liste)
    print(num.output())
    print(text.output())
    print(log.output())