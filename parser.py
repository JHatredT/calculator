from func import func_tbl
from typing import List, Callable
from const import const_tbl


class Parser:
    def parse(self, expr: str) -> float:
        index = 0
        output = []
        op_stack = []

        while index < len(expr):
            if self._is_digit_or_dot(expr, index) or expr[index] in const_tbl:
                index = self._parse_num(expr, index, output)
            elif expr[index] == '(':
                op_stack.append('(')
                index += 1
            elif expr[index] == ')':
                index = self._parse_paren(expr, index, output, op_stack)
            else:
                index = self._parse_func(expr, index, output, op_stack)

        while op_stack and op_stack[-1] in func_tbl:
            self._apply_func(output, op_stack)

        if op_stack or not output or len(output) > 1:
            raise ValueError

        return output[0]

    def _parse_num(self, expr: str, ptr: int, out: List[float]) -> int:
        if expr[ptr] in const_tbl:
            out.append(const_tbl[expr[ptr]])
            ptr += 1
            return ptr

        base = ptr

        while ptr < len(expr) and self._is_digit_or_dot(expr, ptr):
            ptr += 1

        if expr[base:ptr].count('.') > 1:
            raise ValueError

        out.append(float(expr[base:ptr]))
        return ptr

    def _parse_func(
        self,
        expr: str,
        ptr: int,
        out: List[float],
        stack: List[str]
    ):
        if stack and stack[-1] not in func_tbl:
            stack.append(expr[ptr])
            ptr += 1
            return ptr

        base = ptr

        while ptr < len(expr) and not self._is_digit_or_dot(expr, ptr):
            ptr += 1

            if expr[base:ptr] in func_tbl:
                break

        while stack and stack[-1] in func_tbl:
            if not func_tbl[expr[base:ptr]].prio <= func_tbl[stack[-1]].prio:
                break
                
            self._apply_func(out, stack)

        stack.append(expr[base:ptr])
        return ptr

    def _parse_paren(
        self,
        expr: str,
        ptr: int,
        out: List[float],
        stack: List[str]
    ):
        while stack and stack[-1] != '(':
            self._apply_func(out, stack)

        if not stack:
            raise ValueError

        stack.pop()
        ptr += 1
        return ptr

    def _apply_func(self, out: List[float], stack: List[str]):
        if func_tbl[stack[-1]].ari == 2 and len(out) >= 2:
            out.append(func_tbl[stack.pop()](out.pop(-2), out.pop()))
        elif func_tbl[stack[-1]].ari == 1 and out:
            out.append(func_tbl[stack.pop()](out.pop()))
        else:
            raise ValueError

    def _is_digit_or_dot(self, expr: str, ptr: int):
        return expr[ptr].isdigit() or expr[ptr] == '.'