from dataclasses import dataclass
from typing import Literal
from collections.abc import Callable


@dataclass
class ParserContext:
    ptr: int
    state: Literal['unary', 'binary']
    output: list[float]
    stack: list[Callable[..., float], str]