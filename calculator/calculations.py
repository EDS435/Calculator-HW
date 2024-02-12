from decimal import Decimal
from typing import Callable, List
from calculator.calc import Calcs2

class Calcs:
    history: List[Calcs2] = []

    @classmethod
    def add_calculation(cls, calculation: Calcs2):
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calcs2]:
        return cls.history

    @classmethod
    def clear_history(cls):
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calcs2:
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calcs2]:
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]