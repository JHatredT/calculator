from dataclasses import dataclass
from collections.abc import Callable
from operator import abs
from core.func import Function


@dataclass
class Delimiter:
    pair: str
    mod: Function


dlm_table = {
    '(': Delimiter(')', None),
    '|': Delimiter('|', Function(abs, 1))
}