from dataclasses import dataclass
from collections.abc import Callable
from operator import abs


@dataclass
class Delimiter:
    pair: str
    mod: Callable[[float], float] | None


dlm_table = {
    '(': Delimiter(')', None),
    '|': Delimiter('|', abs)
}

