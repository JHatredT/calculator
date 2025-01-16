from parser import Parser
from key import key_grid
from typing import Callable
from tkinter import (
    Tk,
    Entry,
    Frame,
    Button
)


class Calculator():
    def __init__(self, root: Tk) -> None:
        self._parser = Parser()
        self._display = Entry(root, font=('Courier New', 18))
        self._keypad = Frame(root)

    def set_display(self) -> None:
        self._display.pack(pady=10)
        self._display.focus()
        self._display.bind('<KeyPress>', 'break')

    def set_keypad(self, columns: int, rows: int) -> None:
        self._keypad.pack(fill='both', expand=True)

        for i in range(columns):
            self._keypad.columnconfigure(i, weight=1)

        for i in range(rows):
            self._keypad.rowconfigure(i, weight=1)

        for i, string in enumerate(key_grid):
            btn = Button(self._keypad, text=string)
            btn.grid(column=i%columns, row=i//columns, sticky='nsew')

    def set_key_command(self, index: int, comd=Callable[None, None]) -> None:
        self._keypad.winfo_children()[index].config(command=comd)

    def set_default_keys(self) -> None:
        for i, key in enumerate(self._keypad.winfo_children()):
            if key['command']:
                continue

            self.set_key_command(i, lambda x=key['text'] : self.ins_char(x))

    def clear(self) -> None:
        self._display.delete(0, 'end')

    def __get_cursor(self) -> int:
        return self._display.index('insert')

    def increment_cursor(self) -> None:
        self._display.icursor(self.__get_cursor() + 1)

    def decrement_cursor(self) -> None:
        self._display.icursor(self.__get_cursor() - 1)

    def del_char(self) -> None:
        self._display.delete(self.__get_cursor() - 1, self.__get_cursor())

    def get_result(self) -> None:
        result = self._parser.parse(self._display.get())
        self.clear()
        self._display.insert(0, str(result).rstrip('0').rstrip('.'))

    def ins_char(self, char: str) -> None:
        self._display.insert(self.__get_cursor(), char)