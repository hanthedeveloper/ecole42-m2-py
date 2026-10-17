import typing
import abc

class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self.wdata: list[str] = []
        self.counter: int = 0
        self.eleman: int = -1

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
            pass
        else:
            self.eleman += 1
        return (self.eleman, popdata)


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

    def ingest(self, data: dict | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper data")
        if isinstance(data, list):
            for i in data:
                self.wdata.extend(i.keys())
                self.wdata.extend(i.values())
        else:
            self.wdata.append(str(data))


def check_helper(my_dict: dict) -> bool:
    if isinstance(my_dict, dict):
        return (all(isinstance(i, str) for i in my_dict.keys())
        and all(isinstance(i, str) for i in my_dict.values()))
    else:
        return False


if __name__ == "__main__":
    ex_num = NumericProcessor()
    ex_text = TextProcessor()
    ex_log = LogProcessor()

    newlist = [0, 1, 2, 3, 4, 5, 6, 7]

    print(ex1.validate(newlist))
    print(ex1.validate(42))
    print(ex1.ingest(newlist))
    print(ex1.wdata)
    print(ex1.output())
    print(ex1.output())
