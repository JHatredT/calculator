from dataclasses import dataclass
from collections.abc import Callable
from tkinter import (
    Tk
)
from operator import (
    add,
    sub,
    mul,
    truediv
)


@dataclass
class Function:
    body: Callable[[float, float], float]
    prec: int


func_tbl = {
    '+': Function(add, 1),
    '−': Function(sub, 1),
    '×': Function(mul, 2),
    '÷': Function(truediv, 2),
}


def parse(string: str) -> float:
    output = []
    stack = []

    ptr = 0
    end = len(string)

    while ptr < end:
        if string[ptr].isdigit():
            base = ptr

            while ptr < end and string[ptr].isdigit():
                ptr += 1

            output.append(float(string[base:ptr]))
        elif string[ptr] in func_tbl:
            while stack and func_tbl[string[ptr]].prec <= stack[-1].prec:
                if len(output) < 2:
                    raise ValueError

                output.append(stack.pop().body(output.pop(-2), output.pop()))

            stack.append(func_tbl[string[ptr]])

            ptr += 1

    while stack:
        if len(output) < 2:
            raise ValueError

        output.append(stack.pop().body(output.pop(-2), output.pop()))

    if not output or len(output) > 1:
        raise ValueError

    return output[0]


def main() -> None:
    root = Tk()

    root.title('Calculator')

    root.geometry('300x400')
    root.resizable(False, False)

    root.mainloop()

    return


if __name__ == '__main__':
    main()