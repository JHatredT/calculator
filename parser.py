from func import func_tbl
from typing import List, Callable


class Parser:
    def __init__(self):
        self._ptr = 0

    def parse(self, expr: str):
        output = []
        stack = []

        while self._ptr < len(expr):
            if self.is_digit_or_dot(expr):
                output.append(self.parse_num(expr))
            elif expr[self._ptr] in func_tbl:
                self.parse_func(expr, output, stack)

        while stack:
            if len(output) < 2:
                raise ValueError

            output.append(stack.pop()(output.pop(-2), output.pop()))

        if not output or len(output) > 1:
            raise ValueError

        self._ptr = 0
        return output[0]

    def parse_num(self, expr: str):
        base = self._ptr

        while self._ptr < len(expr) and self.is_digit_or_dot(expr):
            self._ptr += 1

        if expr[base:self._ptr].count('.') > 1:
            raise ValueError

        return float(expr[base:self._ptr])

    def parse_func(self, expr: str, output: List[float], stack: List[str]):
        while stack and func_tbl[expr[self._ptr]].prio <= stack[-1].prio:
            if len(output) < 2:
                raise ValueError

            output.append(stack.pop()(output.pop(-2), output.pop()))

        stack.append(func_tbl[expr[self._ptr]])
        self._ptr += 1

    def is_digit_or_dot(self, expr: str):
        return expr[self._ptr].isdigit() or expr[self._ptr] == '.'