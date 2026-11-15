from abc import ABC, abstractmethod
from ex3 import CreatureFactory, TransformCapability


class InvalidStrategy(Exception):
    


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature):
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        creature.attack()

    def is_valid(self) -> bool:
        return True


class AggresiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return if isnstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategy(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )
