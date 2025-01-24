from tkinter import Misc

from tkinter.ttk import (
	Entry,
	Frame
)


class Display(Frame):
	def __init__(self, master: Misc | None = None, **kwargs) -> None:
		super().__init__(master, **kwargs)

		self.display_string = Entry(self, font=("Courier New", 16))
		self.display_string.pack(fill = "both", expand = True, pady = 10)
		self.display_string.focus()
		self.display_string.bind("<KeyPress>", "break")

	def clear_string(self) -> None:
		self.display_string.delete(0, 'end')

	def move_cursor(self, step: int) -> None:
		self.display_string.icursor(self._get_cursor() + step)

	def delete_char(self) -> None:
		self.display_string.delete(self._get_cursor() - 1, self._get_cursor())

	def set_string(self, string: str) -> None:
		self.clear_string()
		self.display_string.insert(0, string)

	def get_string(self) -> None:
		return self.display_string.get()

	def insert_char(self, char: str) -> None:
		self.display_string.insert(self._get_cursor(), char)

	def _get_cursor(self) -> int:
		return self.display_string.index('insert')