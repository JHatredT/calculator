from dataclasses import dataclass
from collections.abc import Callable
from math import sin, cos, tan, asin, acos, atan


@dataclass
class Function:
    _func: Callable[..., float]
    arity: int

    def __call__(self, values: list[float]):
        return self._func(*values)


func_table = {
    'sin': Function(sin, 1),
    'cos': Function(cos, 1),
    'tan': Function(tan, 1),
    'asin': Function(asin, 1),
    'acos': Function(acos, 1),
    'atan': Function(atan, 1),
}