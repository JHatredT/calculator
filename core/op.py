from dataclasses import dataclass
from typing import Literal
from operator import pos, neg, add, sub, mul, truediv, pow
from core.func import Function


@dataclass
class Operator(Function):
    prec: int
    assoc: None | Literal['left', 'right']


unary_op_table = {
    '+': Operator(pos, 1, 3, None),
    '−': Operator(neg, 1, 3, None)
}


binary_op_table = {
    '+': Operator(add, 2, 1, 'left'),
    '−': Operator(sub, 2, 1, 'left'),
    '×': Operator(mul, 2, 2, 'left'),
    '÷': Operator(truediv, 2, 2, 'left'),
    '^': Operator(pow, 2, 4, 'right')
}