import typing
import abc

class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self.newlist: list[str] = []
        self.counter: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return tuple

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

        else:
            newlist = 
class TextProcessor(DataProcessor):





class LogProcessor(DataProcessor):
