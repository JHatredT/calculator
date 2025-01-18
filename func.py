from dataclasses import dataclass
from typing import Callable
from operator import (
    add,
    sub,
    mul,
    truediv
)
from math import (
    sin,
    cos,
    tan,
    asin,
    acos,
    atan
)


@dataclass
class Function:
    __func: Callable[..., float]
    prio: int
    ari: int

    def __call__(self, *args: float):
        return self.__func(*args)


func_tbl = {
    '+': Function(add, 1, 2),
    '−': Function(sub, 1, 2),
    '×': Function(mul, 2, 2),
    '÷': Function(truediv, 2, 2),
    'sin': Function(sin, 3, 1),
    'cos': Function(cos, 3, 1),
    'tan': Function(tan, 3, 1),
    'asin': Function(asin, 3, 1),
    'acos': Function(acos, 3, 1),
    'atan': Function(atan, 3, 1)
}