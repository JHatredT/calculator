from dataclasses import dataclass
from typing import Callable
from operator import (
    add,
    sub,
    mul,
    truediv
)


@dataclass
class Function:
    __func: Callable[..., float]
    prio: int

    def __call__(self, *args: float):
        return self.__func(*args)


func_tbl = {
    '+': Function(add, 1),
    '−': Function(sub, 1),
    '×': Function(mul, 2),
    '÷': Function(truediv, 2),
}