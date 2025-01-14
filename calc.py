from func import func_tbl
from key import key_grid
from typing import List, Callable
from tkinter import (
    Tk,
    Entry,
    Frame,
    Button
)


class Calculator():
    def __init__(self, root: Tk) -> None:
        self.__ptr = 0
        self.__display = Entry(root, font=('Courier New', 18))
        self.__keypad = Frame(root)

    def set_display(self) -> None:
        self.__display.pack(pady=10)
        self.__display.focus()
        self.__display.bind('<KeyPress>', 'break')

    def set_keypad(self, columns: int, rows: int) -> None:
        self.__keypad.pack(fill='both', expand=True)

        for i in range(columns):
            self.__keypad.columnconfigure(i, weight=1)

        for i in range(rows):
            self.__keypad.rowconfigure(i, weight=1)

        for i, string in enumerate(key_grid):
            btn = Button(self.__keypad, text=string)
            btn.grid(column=i%columns, row=i//columns, sticky='nsew')

    def set_key_command(self, index: int, comd=Callable[None, None]) -> None:
        self.__keypad.winfo_children()[index].config(command=comd)

    def set_default_keys(self) -> None:
        for i, key in enumerate(self.__keypad.winfo_children()):
            if key['command']:
                continue

            self.set_key_command(i, lambda x=key['text'] : self.ins_char(x))

    def clear(self) -> None:
        self.__display.delete(0, 'end')

    def __get_cursor(self) -> int:
        return self.__display.index('insert')

    def increment_cursor(self) -> None:
        self.__display.icursor(self.__get_cursor() + 1)

    def decrement_cursor(self) -> None:
        self.__display.icursor(self.__get_cursor() - 1)

    def del_char(self) -> None:
        self.__display.delete(self.__get_cursor() - 1, self.__get_cursor())

    def get_result(self) -> None:
        result = self.__parse()
        self.clear()
        self.__display.insert(0, str(result).rstrip('0').rstrip('.'))

    def ins_char(self, char: str) -> None:
        self.__display.insert(self.__get_cursor(), char)

    def __parse(self) -> None:
        output = []
        stack = []
        
        while not self.__is_end():
            if self.__is_num():
                self.__parse_num(output)
            elif self.__is_func():
                self.__parse_func(output, stack)

        while stack:
            if len(output) < 2:
                raise ValueError

            output.append(stack.pop()(output.pop(-2), output.pop()))

        if not output or len(output) > 1:
            raise ValueError

        self.__ptr = 0
        return output[0]

    def __parse_num(self, output: List[float]) -> None:
        base = self.__ptr

        while not self.__is_end() and self.__is_num():
            self.__ptr += 1

        if self.__display.get()[base:self.__ptr].count('.') > 1:
            raise(ValueError)

        output.append(float(self.__display.get()[base:self.__ptr]))

    def __parse_func(self, output: List[float], stack: List[str]) -> None:
        while stack and func_tbl[self.__get_char()].prio <= stack[-1].prio:
            if len(output) < 2:
                raise ValueError

            output.append(stack.pop()(output.pop(-2), output.pop()))

        stack.append(func_tbl[self.__get_char()])
        self.__ptr += 1

    def __is_end(self) -> bool:
        return self.__ptr >= len(self.__display.get())

    def __is_num(self) -> bool:
        return self.__get_char().isdigit() or self.__get_char() == '.'

    def __is_func(self) -> bool:
        return self.__get_char() in func_tbl

    def __get_char(self) -> str:
        return self.__display.get()[self.__ptr]