from abc import ABC, abstractmethod
from ex3 import TransformCapability, Creature


class InvalidStrategy(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        creature.attack()

    def is_valid(self) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategy(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())